from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    #phone = forms.IntegerField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1','password2', 'first_name', 'phone', 'systemid' ]
        

class CustomLoginForm(AuthenticationForm):
    # Add custom fields or override default behavior
    pass