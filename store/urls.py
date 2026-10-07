from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:pk>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
]
