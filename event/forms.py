#from .models import List
#from django.views.generic import ListView
from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import UserProfile
from .models import Organiser
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    #phone = forms.IntegerField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1','password2', 'first_name', 'phone', 'systemid' ]

class RegistrationForm2(forms.Form):
    your_school = forms.ChoiceField(choices=settings.PROGRAMMING_LANGUAGES)

'''
class RegistrationForm(forms.Form):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1','password2', 'first_name', 'phone', 'systemid' ]
    
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = User()
        user.save()
        return user

class RegistrationForm2(forms.Form):

    class Meta:
        model = UserProfile
        
        your_school = forms.ChoiceField(choices=settings.PROGRAMMING_LANGUAGES)

    

    
    def save(self, commit=True):
        user = super(RegistrationForm2, self).save(commit=False)
        # Additional processing or modifications to the user object if needed
        if commit:
            user.save()
        return user
    
'''

class CreateEvent(forms.ModelForm):

    class Meta:
        model = Organiser
        fields = ['user_id', 'event_type', 'name_of_event', 'description', 'department', 'for_batch', 'date', 'venue', 'time', 'mode', 'organiser_name', 'organiser_phone', 'organiser_email', 'last_date_to_register' ]

'''
class EventList(ListView):
    model = List
    template_name = 'event_list.html'  # Specify the template to use
    context_object_name = 'events'  # Specify the variable name in the template for the object list
'''