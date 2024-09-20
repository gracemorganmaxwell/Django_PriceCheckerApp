from django.contrib import admin
from django.urls import path, include
from .views import register_view 
from django.contrib.auth import views as auth_views
from .views import HomePageView, store_preference_view, product_list_view, product_detail, CartView, CheckoutView, store_select, add_to_cart, remove_from_cart, update_cart, remove_store_preference
from .forms import EmailOrUsernameLoginForm
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
   path('signup/', register_view, name='signup' ),
    path('', product_list_view, name='product_list'),
    path('home/', HomePageView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'  
    ), name='login'),    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('store-preference/', store_preference_view, name='store_preference'),
    path('store/<int:store_id>/', views.store_select, name='store_select'),
    path('products/', product_list_view, name='product_list'),
    path('products/<int:product_id>/', product_detail, name='product_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/update/', update_cart, name='update_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('favorites/remove/<int:product_id>/', views.remove_favorite, name='remove_favorite'),
    path('remove_store_preference/<int:store_id>/', remove_store_preference, name='remove_store_preference'),
    path('product/<int:product_id>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('toggle_favorite/<int:product_id>/', views.toggle_favorite, name='toggle_favorite'),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
