from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from django.db import IntegrityError
from .models import UserStorePreference, Store, FavoriteProduct, Product, CartItem, PriceHistory
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
import json

# Homepage View
class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'super/home.html'
    login_url = '/login/'
    redirect_field_name = 'next'

    # Get user's preferences and favorite products
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            store_preferences = UserStorePreference.objects.filter(user=self.request.user)
            context['store_preferences'] = store_preferences
            
            favorite_products = FavoriteProduct.objects.filter(user=self.request.user)
            context['favorite_products'] = favorite_products

        return context

# Toggle favorite status of a product
def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    favorite_product, created = FavoriteProduct.objects.get_or_create(user=request.user, product=product)

    if not created:
        favorite_product.delete()
        messages.success(request, f"{product.product_name} was removed from your favorites.")
    else:
        messages.success(request, f"{product.product_name} was added to your favorites.")

    return redirect('product_detail', product_id=product_id)

# User registration view
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.first_name = form.cleaned_data.get('first_name')
                user.last_name = form.cleaned_data.get('last_name')
                user.email = form.cleaned_data.get('email')
                user.save()
                return redirect('login')
            except IntegrityError:
                form.add_error('username', 'This username is already taken. Please choose another one.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Placeholder for store preference feature
def placeholder_view(request):
    return HttpResponse("Store preference feature coming soon!")

# Store preference view
@login_required
def store_preference_view(request):
    store_preferences = UserStorePreference.objects.filter(user=request.user)
    stores = Store.objects.all()

    if request.method == 'POST':
        store_id = request.POST.get('store')
        store = Store.objects.get(store_id=store_id)
        UserStorePreference.objects.create(user=request.user, store=store)
        return redirect('store_preference')
    
    context = {
        'store_preferences': store_preferences,
        'stores': stores
    }
    return render(request, 'super/store_preference.html', context)

# Product list view with search, category filter, and sorting
def product_list_view(request):
    categories = Product.objects.values_list('product_category', flat=True).distinct()
    query = request.GET.get('q', '')  
    selected_category = request.GET.get('category', '') 
    sort_by = request.GET.get('sort', 'no_price')  # Default to 'no_price'

    # Filter products based on search and category
    products = Product.objects.all()
    if query:
        products = products.filter(product_name__icontains=query)
    if selected_category:
        products = products.filter(product_category=selected_category)

    # Apply sorting based on the 'sort_by' parameter
    if sort_by == 'lowest_price':
        products = products.order_by('unit_price')
    elif sort_by == 'highest_price':
        products = products.order_by('-unit_price')

    # Handle favorite products (for authenticated users)
    favorite_products = []
    if request.user.is_authenticated:
        favorite_products = FavoriteProduct.objects.filter(user=request.user).values_list('product__product_id', flat=True)

    # Get cart items and session cart
    cart_items = CartItem.objects.filter(user=request.user).values_list('product__product_id', flat=True)
    cart = request.session.get('cart', {})

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'query': query,  
        'favorite_products': favorite_products,
        'cart_items': cart_items,
        'cart': cart
    }
    return render(request, 'super/product_list.html', context)

# Product detail view with price history and favorite functionality
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    price_history = PriceHistory.objects.filter(product=product).order_by('date')

    # Prepare data for the price history chart
    price_data = [float(history.price) for history in price_history]
    date_data = [history.date.strftime('%Y-%m-%d') for history in price_history]

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if product_id and product_id.isdigit():
            product = get_object_or_404(Product, product_id=product_id)
            favorite, created = FavoriteProduct.objects.get_or_create(user=request.user, product=product)
            if not created:
                favorite.delete()
        return redirect('product_detail')

    favorite_products = FavoriteProduct.objects.filter(user=request.user).values_list('product__product_id', flat=True)
    cart_items = CartItem.objects.filter(user=request.user).values_list('product_id', flat=True)
    cart = request.session.get('cart', {})

    return render(request, 'super/product_detail.html', {
        'product': product,
        'favorite_products': list(favorite_products),
        'price_data': json.dumps(price_data),
        'date_data': json.dumps(date_data),
        'cart_items': cart_items,
        'cart': cart
    })

# Cart view to display items in the cart
class CartView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        cart_items = []
        total_amount = 0

        for product_id, details in cart.items():
            product = get_object_or_404(Product, product_id=int(product_id))
            quantity = details['quantity']
            total_price = float(details['price']) * quantity
            total_amount += total_price

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total_price': total_price
            })

        context = {
            'cart_items': cart_items,
            'total_amount': total_amount
        }
        return render(request, 'super/cart.html', context)

# Add product to cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str]['quantity'] += 1
        messages.info(request, f'{product.product_name} quantity updated in your cart.')
    else:
        cart[product_id_str] = {
            'name': product.product_name,
            'price': str(product.unit_price),  # Store price as string for JSON compatibility
            'quantity': 1
        }
        messages.success(request, f'{product.product_name} has been added to your cart.')

    request.session['cart'] = cart
    return redirect('product_list')

# Remove product from cart
def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    product_id_str = str(item_id)

    if product_id_str in cart:
        del cart[product_id_str]
        request.session['cart'] = cart
        messages.success(request, 'Item removed from cart.')

    return redirect('cart')

# Update cart quantities
def update_cart(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})
        for key in request.POST:
            if key.startswith('quantity_'):
                product_id = key.split('_')[1]
                new_quantity = int(request.POST.get(key, 1))
                if new_quantity > 0:
                    if product_id in cart:
                        cart[product_id]['quantity'] = new_quantity
        request.session['cart'] = cart
        return redirect('cart')

# Checkout view to handle cart checkout
class CheckoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        cart_items = CartItem.objects.filter(user=request.user)
        total_amount = sum(item.total_price for item in cart_items)
        context = {
            'cart_items': cart_items,
            'total_amount': total_amount
        }

# Store select view
@login_required
def store_select(request, store_id):
    store = get_object_or_404(Store, store_id=store_id)
    all_stores = Store.objects.all()
    
    if request.method == 'POST':
        selected_store_id = request.POST.get('store_id')
        selected_store = get_object_or_404(Store, store_id=selected_store_id)
        UserStorePreference.objects.get_or_create(user=request.user, store=selected_store)
        return redirect('store_preference')
    
    context = {
        'store': store,
        'all_stores': all_stores,
    }
    return render(request, 'super/store_select.html', context)
 
# Remove store preference
@login_required
def remove_store_preference(request, store_id):
    store = get_object_or_404(Store, store_id=store_id)
    UserStorePreference.objects.filter(user=request.user, store=store).delete()
    messages.success(request, f"{store.store_name} has been removed from your preferences.")
    return redirect('store_preference')

def remove_favorite(request, product_id):
    favorite = get_object_or_404(FavoriteProduct, user=request.user, product__product_id=product_id)
    favorite.delete()
    return redirect('home')  # Redirect to the homepage or another page as needed