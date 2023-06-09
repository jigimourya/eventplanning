from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import CustomUser
from .models import Organiser
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    #phone = forms.IntegerField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1','password2', 'first_name', 'phone', 'systemid' ]

class RegistrationForm2(forms.Form):
    your_school = forms.ChoiceField(choices=settings.PROGRAMMING_LANGUAGES)


class CreateEvent(forms.ModelForm):

    class Meta:
        model = Organiser
        fields = ['title', 'description', 'date', 'location']
'''
class CustomLoginForm(AuthenticationForm):
    # Add custom fields or override default behavior
    pass
'''