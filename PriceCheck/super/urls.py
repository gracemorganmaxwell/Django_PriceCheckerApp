from django.contrib import admin
from django.urls import path, include
from .views import register_view 
from django.contrib.auth import views as auth_views
from .views import HomePageView, store_preference_view, product_list_view, product_detail, CartView, RemoveFromCartView, CheckoutView
from .forms import EmailOrUsernameLoginForm
from . import views



urlpatterns = [
   path('signup/', register_view, name='signup' ),
    path('', product_list_view, name='product_list'),
    path('home/', HomePageView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'  
    ), name='login'),    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('store-preference/', store_preference_view, name='store_preference'),
    path('products/', product_list_view, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/remove/<int:item_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]
