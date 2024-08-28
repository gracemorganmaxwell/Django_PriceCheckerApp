from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def register_view(request):
    print("Register view called")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html',  {'form' : form})