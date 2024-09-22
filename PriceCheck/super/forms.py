from django import forms
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import get_user_model

class EmailOrUsernameLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username or Email",
        widget=forms.TextInput(attrs={'autofocus': True})
    )

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text="Required. Enter your first name.")
    last_name = forms.CharField(max_length=30, required=True, help_text="Required. Enter your last name.")
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")
    usable_password = None

class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
