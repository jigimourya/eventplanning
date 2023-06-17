from typing import Type
from django.shortcuts import render, redirect
from .models import Organiser
#from event.models import Organiser
from .forms import CreateEvent, RegistrationForm
from .forms import RegistrationForm2
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register2')
              # Redirect to login page
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            # Process form data
            # Redirect or show success message
    else:
        form = RegistrationForm2()
    return render(request, 'registration/register2.html', {'form': form})

def login_view(request):
    errorMessage = ""
    if request.method == 'POST':
        print("in post")
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(username)
        user = authenticate(username=username, password = password)
        print("authenticated")
        print(user)
        if user is not None:
            print('user found')
            if user.is_active:
                print('user active')
                login(request, user)
                return redirect('loginhomepage')
        else:
            errorMessage = 'Invalid username/password, try again'
    print("loginpage")
    return render(request, 'login.html', {'errorMessage': errorMessage})
   
def homepage2(request):
    # Your homepage logic
    return render(request, 'loginhomepage.html')

def create_event(request):
    if request.method == 'POST':
        form = CreateEvent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
              # Redirect to login page
    else:
        form = CreateEvent()
    return render(request, 'create_event.html', {'form': form})

def event_list(request):
    event = Organiser.objects.all()
    return render(request, 'event_list.html', {'event': event})

def homepage(request):

    print(request.user.username)

    # Your homepage logic
    return render(request, 'homepage.html')