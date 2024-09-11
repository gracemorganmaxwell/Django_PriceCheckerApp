from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm
from django.db import IntegrityError
from .models import UserStorePreference
from django.http import HttpResponse


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'super/home.html'
    login_url = '/login/'  
    redirect_field_name = 'next'  

            #  Gets users store preference
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:  
            store_preferences = UserStorePreference.objects.filter(user=self.request.user)
            context['store_preferences'] = store_preferences
        return context





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
