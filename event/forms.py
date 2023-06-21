from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .models import Organiser
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1','password2', 'first_name', 'phone', 'systemid' ]



class RegistrationForm2(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['your_school']
    #your_school = forms.ChoiceField(choices=settings.PROGRAMMING_LANGUAGES)



class CreateEvent(forms.ModelForm):

    class Meta:
        model = Organiser
        fields = ['id', 'user_id', 'event_type', 'name_of_event', 'description', 'department', 'for_batch', 'date', 'venue', 'time', 'mode', 'organiser_name', 'organiser_phone', 'organiser_email', 'last_date_to_register' ]
