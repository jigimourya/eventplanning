#from .models import List
#from django.views.generic import ListView
from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import CustomUser, UserProfile
from .models import Organiser
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings

class RegistrationForm(UserCreationForm):
  
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1','password2', 'first_name', 'phone', 'systemid' ]

class RegistrationForm2(forms.Form):

    class Meta:
        model = UserProfile
        your_school = forms.ChoiceField(choices=settings.PROGRAMMING_LANGUAGES)


class CreateEvent(forms.ModelForm):

    class Meta:
        model = Organiser
        fields = ['event_type', 'name_of_event', 'description', 'department', 'for_batch', 'date', 'venue', 'time', 'mode', 'organiser_name', 'organiser_phone', 'organiser_email', 'last_date_to_register' ]

'''
class EventList(ListView):
    model = List
    template_name = 'event_list.html'  # Specify the template to use
    context_object_name = 'events'  # Specify the variable name in the template for the object list
'''