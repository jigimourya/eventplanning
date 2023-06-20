from typing import Type
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from .models import Organiser
#from event.models import Organiser
from .forms import CreateEvent, RegistrationForm
from .forms import RegistrationForm2
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth import get_user
from django.contrib.auth import logout


def register(request):
    if isUserLoggedIn(request):
        return redirect('homepage')

    if request.method == 'POST':
        print('register')
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('login')
              # Redirect to login page
        else:
            print('not valid')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def registration_view(request):
    if isUserLoggedIn(request):
        return redirect('homepage')

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
    if isUserLoggedIn(request):
        return redirect('homepage')

    errorMessage = ""
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password = password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('homepage')
        else:
            errorMessage = 'Invalid username/password, try again'
    print("loginpage")
    return render(request, 'login.html', {'errorMessage': errorMessage})
   
def homepage2(request):
    user = get_user(request)
    # Your homepage logic
    return render(request, 'loginhomepage.html')

def create_event(request):
    if not isUserLoggedIn(request):
        return redirect('register')

    isLoggedIn = isUserLoggedIn(request)

    if isLoggedIn:
        loggedInUserName = getLoggedInUserName(request)
    else:
        loggedInUserName = ''

    if request.method == 'POST':
        form = CreateEvent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
              # Redirect to login page
    else:
        form = CreateEvent()
    return render(request, 'create_event.html', {'form': form, 'isLoggedIn': isLoggedIn, 'loggedInUserName': loggedInUserName})

def event_list(request):
    isLoggedIn = isUserLoggedIn(request)

    if isLoggedIn:
        loggedInUserName = getLoggedInUserName(request)
    else:
        loggedInUserName = ''
    events = Organiser.objects.filter(user=request.user)
    return render(request, 'event_list.html', {'events': events, 'isLoggedIn': isLoggedIn, 'loggedInUserName': loggedInUserName})

def homepage(request):
    isLoggedIn = isUserLoggedIn(request)

    if isLoggedIn:
        loggedInUserName = getLoggedInUserName(request)
    else:
        loggedInUserName = ''

    

    # Your homepage logic
    return render(request, 'homepage.html', {'isLoggedIn': isLoggedIn, 'loggedInUserName': loggedInUserName})


def getLoggedInUserName(request):
    user = get_user(request)
    return user.username


def isUserLoggedIn(request):
    user = get_user(request)

    if user.is_authenticated:
        print("Authenticated")
        username = user.username
        print("Authenticated2")
    else:
        # User is not logged in
        print("not Authenticated")
        username = None
    return username

def logout_view(request):
    logout(request)
    return redirect('homepage')