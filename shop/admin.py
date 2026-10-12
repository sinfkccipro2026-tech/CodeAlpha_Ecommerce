from django.contrib import admin
from .models import Product, Order, OrderItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','price','stock','created_at')
    search_fields = ('name','category')
    list_filter = ('category',)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','total','status','created_at')
    list_filter = ('status','created_at')
    search_fields = ('user__username','full_name','email')
    inlines = [OrderItemInline]
