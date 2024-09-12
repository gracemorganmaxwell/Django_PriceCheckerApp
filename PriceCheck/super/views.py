from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from django.db import IntegrityError
from .models import UserStorePreference, Store, FavoriteProduct, Product
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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
        store = Store.objects.get(id=store_id)

        UserStorePreference.objects.create(user=request.user, store=store)
        return redirect('store_preference')
    
    context = {
        'store_preferences' : store_preferences,
        'stores' : stores
    }
    return render(request, 'super/store_preference.html', context)

#product list view
def product_list_view(request):
   
    categories = Product.objects.values_list('product_category', flat=True).distinct()

    
    selected_category = request.GET.get('category', '')

   
    if selected_category:
        products = Product.objects.filter(product_category=selected_category)
    else:
        products = Product.objects.all()  

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category  
    }
    return render(request, 'super/product_list.html', context)
