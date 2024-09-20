from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from django.db import IntegrityError
from .models import UserStorePreference, Store, FavoriteProduct, Product, CartItem, PriceHistory, CartItem
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
import json
from django.core.paginator import Paginator


#Homepage View
class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'super/home.html'
    login_url = '/login/'
    redirect_field_name = 'next'

        # get users preferences
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            
            store_preferences = UserStorePreference.objects.filter(user=self.request.user)
            context['store_preferences'] = store_preferences
            
            
            favorite_products = FavoriteProduct.objects.filter(user=self.request.user)
            context['favorite_products'] = favorite_products

        return context

def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    favorite_product, created = FavoriteProduct.objects.get_or_create(user=request.user, product=product)

    if not created:
        # If the product is already a favorite, remove it
        favorite_product.delete()
        messages.success(request, f"{product.product_name} was removed from your favorites.")
    else:
        # If it's not a favorite, add it
        messages.success(request, f"{product.product_name} was added to your favorites.")

    return redirect('product_detail', product_id=product_id)

#sign up view
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



def placeholder_view(request):
    return HttpResponse("Store preference feature coming soon!")


#store preference view
@login_required
def store_preference_view(request):
    store_preferences = UserStorePreference.objects.filter(user=request.user)
    
    stores = Store.objects.all()

    if request.method == 'POST':
        store_id = request.POST.get('store')
        store = Store.objects.get(store_id=store_id)
        user = request.user
        
        UserStorePreference.objects.create(user=request.user, store=store)
        return redirect('store_preference')
    
    context = {
        'store_preferences' : store_preferences,
        'stores' : stores
    }
    return render(request, 'super/store_preference.html', context)

#product list view
@login_required
def product_list_view(request):
    categories = Product.objects.values_list('product_category', flat=True).distinct()
    query = request.GET.get('q', '')  
    selected_category = request.GET.get('category', '') 
    sort_by = request.GET.get('sort', 'no_price')

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

    # Prefetch or bulk-fetch price history
    price_histories = PriceHistory.objects.filter(product__in=products).order_by('product', '-date')

    # Create a dictionary to store the latest and previous prices
    price_data = {}
    for price_history in price_histories:
        product_id = price_history.product_id
        if product_id not in price_data:
            price_data[product_id] = {'latest_price': price_history.price, 'previous_price': None}
        elif price_data[product_id]['previous_price'] is None:
            price_data[product_id]['previous_price'] = price_history.price

    # Calculate the price trend for each product and print out the trend
    product_data = []
    for product in products:
        trend = None
        if product.product_id in price_data:
            current = price_data[product.product_id]['latest_price']
            previous = price_data[product.product_id]['previous_price']
            print(f"Product: {product.product_name}, Current Price: {current}, Previous Price: {previous}")  # Debugging

            if previous is not None and current is not None:
                if current > previous:
                    trend = 'up'
                elif current < previous:
                    trend = 'down'
                else:
                    trend = 'same'
            print(f"Trend for {product.product_name}: {trend}")  # Debugging
        
        product_data.append({
            'product': product,
            'price_trend': trend,
        })

    

    # Now apply pagination to the constructed 'product_data'
    paginator = Paginator(product_data, 10)  # Show 10 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Handle the rest of the context and logic
    favorite_products = FavoriteProduct.objects.filter(user=request.user).values_list('product__product_id', flat=True)
    cart_items = CartItem.objects.filter(user=request.user).values_list('product__product_id', flat=True)

    context = {
        'page_obj': page_obj,  # Pass the paginated data to the template
        'categories': categories,
        'selected_category': selected_category,
        'query': query,  
        'favorite_products': favorite_products,
        'cart_items': cart_items,  # Pass the cart items to the template
        'cart': request.session.get('cart', {}),  # Pass session cart
    }

    return render(request, 'super/product_list.html', context)


    
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    price_history = PriceHistory.objects.filter(product=product).order_by('date')

    # Prepare data for the chart
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
    
    cart = request.session.get('cart', {})
    cart_items = CartItem.objects.filter(user=request.user).values_list('product_id', flat=True)
    cart = CartItem(request)

    if len(cart_items) > 2:
        print(cart_items[2])  # Safely accessing the third cart item
    else:
        print("Less than 3 items in the cart.")
    
    return render(request, 'super/product_detail.html', {
        'product': product,
        'favorite_products': list(favorite_products),
        'price_data': json.dumps(price_data),  # Convert to JSON
        'date_data': json.dumps(date_data),    # Convert to JSON
        'cart_items': cart_items,
        'cart': cart

    })


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

    
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    
    # Get the current cart from session or initialize an empty cart
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    cart = request.session.get('cart', {})

    # Convert product_id to a string since session keys are stored as strings
    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str]['quantity'] += 1
        messages.info(request, f'{product.product_name} quantity updated in your cart.')
    else:
        cart[product_id_str] = {
            'name': product.product_name,
            'price': str(product.unit_price),  # Store price as string to prevent JSON issues
            'quantity': 1
        }
        messages.success(request, f'{product.product_name} has been added to your cart.')

    # Update the session cart
    request.session['cart'] = cart
    return redirect('product_list')  # Redirect to cart page



def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})

    product_id_str = str(item_id)

    if product_id_str in cart:
        del cart[product_id_str]
        request.session['cart'] = cart
        messages.success(request, 'Item removed from cart.')

    return redirect('cart')

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

class CheckoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        cart_items = CartItem.objects.filter(user=request.user)
        total_amount = sum(item.total_price for item in cart_items)
        context = {
            'cart_items': cart_items,
            'total_amount': total_amount
        }
        return render(request, 'super/checkout.html', context)

    def post(self, request, *args, **kwargs):
        # Handle the checkout process (e.g., creating an order, processing payment)
        CartItem.objects.filter(user=request.user).delete()  # Clear the cart after checkout
        return redirect('home')  # Redirect to a thank you page or home
    
def store_select(request, store_id):
    store = get_object_or_404(Store, store_id=store_id)
    all_stores = Store.objects.all()  # Fetch all stores to populate the dropdown
    # all_stores = Store.objects.filter(chain_id=store.chain_id)
    return render(request, 'super/store_select.html', {'store': store, 'all_stores': all_stores})

from django.shortcuts import get_object_or_404, redirect
from .models import FavoriteProduct

def remove_favorite(request, product_id):
    favorite = get_object_or_404(FavoriteProduct, user=request.user, product__product_id=product_id)
    favorite.delete()
    return redirect('home')  # Redirect to the homepage or another page as needed


@login_required
def remove_store_preference(request, store_id):
    # Get the store preference object
    preference = get_object_or_404(UserStorePreference, user=request.user, store_id=store_id)
    
    # Delete the store preference
    preference.delete()
    
    # Redirect back to the store preferences page
    return redirect('store_preference')

def get_cart_items(self):
    # Assuming cart_items is a dictionary of product_id and quantity
    return {str(item['product_id']): item['quantity'] for item in self.cart}
