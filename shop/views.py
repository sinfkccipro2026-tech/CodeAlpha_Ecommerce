from decimal import Decimal
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Order, OrderItem


def home(request):
    products = Product.objects.all()
    q = request.GET.get('q','').strip()
    category = request.GET.get('category','').strip()
    if q:
        products = products.filter(name__icontains=q)
    if category:
        products = products.filter(category=category)
    categories = Product.objects.values_list('category', flat=True).distinct().order_by('category')
    return render(request, 'shop/home.html', {'products': products, 'categories': categories, 'q': q, 'category': category})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save(); login(request, user)
        messages.success(request, 'Account created successfully.')
        return redirect('home')
    return render(request, 'shop/register.html', {'form': form})

def _get_cart(request):
    return request.session.setdefault('cart', {})

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = _get_cart(request)
    key = str(pk)
    current = int(cart.get(key, 0))
    if current < product.stock:
        cart[key] = current + 1
        request.session.modified = True
        messages.success(request, f'{product.name} added to cart.')
    else:
        messages.error(request, 'Requested quantity is not available.')
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def cart(request):
    raw = request.session.get('cart', {})
    products = Product.objects.filter(id__in=[int(k) for k in raw.keys()])
    items=[]; total=Decimal('0.00')
    for p in products:
        qty=min(int(raw.get(str(p.id),0)), p.stock)
        subtotal=p.price*qty; total += subtotal
        items.append({'product':p,'quantity':qty,'subtotal':subtotal})
    return render(request,'shop/cart.html',{'items':items,'total':total})

def update_cart(request, pk):
    product=get_object_or_404(Product,pk=pk); qty=max(0,int(request.POST.get('quantity',1)))
    cart=_get_cart(request)
    if qty == 0: cart.pop(str(pk),None)
    else: cart[str(pk)] = min(qty, product.stock)
    request.session.modified=True
    return redirect('cart')

def remove_from_cart(request, pk):
    cart=_get_cart(request); cart.pop(str(pk),None); request.session.modified=True
    return redirect('cart')

@login_required
def checkout(request):
    raw=request.session.get('cart',{})
    products=Product.objects.filter(id__in=[int(k) for k in raw.keys()])
    items=[]; total=Decimal('0.00')
    for p in products:
        qty=int(raw.get(str(p.id),0))
        if qty > p.stock: messages.error(request, f'Only {p.stock} units of {p.name} are available.'); return redirect('cart')
        if qty: items.append((p,qty)); total += p.price*qty
    if not items: return redirect('cart')
    if request.method=='POST':
        data=request.POST
        if not all(data.get(k,'').strip() for k in ['full_name','email','phone','address','city','pincode']):
            messages.error(request,'Please fill all delivery details.'); return render(request,'shop/checkout.html',{'total':total})
        with transaction.atomic():
            order=Order.objects.create(user=request.user,full_name=data['full_name'],email=data['email'],phone=data['phone'],address=data['address'],city=data['city'],pincode=data['pincode'],total=total)
            for p,qty in items:
                OrderItem.objects.create(order=order,product=p,quantity=qty,price=p.price)
                p.stock -= qty; p.save(update_fields=['stock'])
        request.session['cart']={}; request.session.modified=True
        return render(request,'shop/order_success.html',{'order':order})
    return render(request,'shop/checkout.html',{'total':total})

@login_required
def orders(request):
    return render(request,'shop/orders.html',{'orders':Order.objects.filter(user=request.user).prefetch_related('items__product')})
