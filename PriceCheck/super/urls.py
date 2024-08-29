from django.contrib import admin
from django.urls import path, include
from .views import register_view 
from django.contrib.auth import views as auth_views
from .views import HomePageView
from .forms import EmailOrUsernameLoginForm


urlpatterns = [
   path('signup/', register_view, name='signup' ),
    path('', HomePageView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(authentication_form=EmailOrUsernameLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]