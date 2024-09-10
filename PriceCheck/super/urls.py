from django.contrib import admin
from django.urls import path, include
from .views import register_view 
from django.contrib.auth import views as auth_views
from .views import HomePageView
from .forms import EmailOrUsernameLoginForm
from .views import (
    SupermarketChainListView, SupermarketChainDetailView, SupermarketChainCreateView, 
    SupermarketChainUpdateView, SupermarketChainDeleteView,
    StoreListView, StoreDetailView, StoreCreateView, StoreUpdateView, StoreDeleteView,
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    PriceHistoryListView, PriceHistoryDetailView, PriceHistoryCreateView, PriceHistoryUpdateView, PriceHistoryDeleteView,
    UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView,
    UserStorePreferenceListView, UserStorePreferenceDetailView, UserStorePreferenceCreateView, UserStorePreferenceUpdateView, UserStorePreferenceDeleteView
)



urlpatterns = [
   path('signup/', register_view, name='signup' ),
    path('', HomePageView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(authentication_form=EmailOrUsernameLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

     # SupermarketChain URLs
    path('supermarket-chains/', SupermarketChainListView.as_view(), name='supermarket-chain-list'),
    path('supermarket-chains/<int:pk>/', SupermarketChainDetailView.as_view(), name='supermarket-chain-detail'),
    path('supermarket-chains/create/', SupermarketChainCreateView.as_view(), name='supermarket-chain-create'),
    path('supermarket-chains/<int:pk>/update/', SupermarketChainUpdateView.as_view(), name='supermarket-chain-update'),
    path('supermarket-chains/<int:pk>/delete/', SupermarketChainDeleteView.as_view(), name='supermarket-chain-delete'),

    # Store URLs
    path('stores/', StoreListView.as_view(), name='store-list'),
    path('stores/<int:pk>/', StoreDetailView.as_view(), name='store-detail'),
    path('stores/create/', StoreCreateView.as_view(), name='store-create'),
    path('stores/<int:pk>/update/', StoreUpdateView.as_view(), name='store-update'),
    path('stores/<int:pk>/delete/', StoreDeleteView.as_view(), name='store-delete'),

    # Product URLs
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    # PriceHistory URLs
    path('pricehistory/', PriceHistoryListView.as_view(), name='pricehistory-list'),
    path('pricehistory/<int:pk>/', PriceHistoryDetailView.as_view(), name='pricehistory-detail'),
    path('pricehistory/create/', PriceHistoryCreateView.as_view(), name='pricehistory-create'),
    path('pricehistory/<int:pk>/update/', PriceHistoryUpdateView.as_view(), name='pricehistory-update'),
    path('pricehistory/<int:pk>/delete/', PriceHistoryDeleteView.as_view(), name='pricehistory-delete'),

    # User URLs
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),

    # UserStorePreference URLs
    path('userstorepreferences/', UserStorePreferenceListView.as_view(), name='userstorepreferance-list'),
    path('userstorepreferences/<int:pk>/', UserStorePreferenceDetailView.as_view(), name='userstorepreferance-detail'),
    path('userstorepreferences/create/', UserStorePreferenceCreateView.as_view(), name='userstorepreferance-create'),
    path('userstorepreferences/<int:pk>/update/', UserStorePreferenceUpdateView.as_view(), name='userstorepreferance-update'),
    path('userstorepreferences/<int:pk>/delete/', UserStorePreferenceDeleteView.as_view(), name='userstorepreferance-delete'),
]

