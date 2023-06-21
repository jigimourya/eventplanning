from typing import Type
from wsgiref.util import request_uri
from django.shortcuts import render, redirect, get_object_or_404
from .models import Organiser
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
            return redirect('register2')
              
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
            
    else:
        form = RegistrationForm2()
    return render(request, 'registration/register.html', {'form': form})

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
   


def create_event(request):
    if not isUserLoggedIn(request):
        return redirect('register')

    isLoggedIn = isUserLoggedIn(request)

    if isLoggedIn:
        loggedInUserName = getLoggedInUserName(request)
    else:
        loggedInUserName = ''

    if request.method == 'POST':

        updated_request = request.POST.copy()
        print(updated_request)
        user_id=getUserId(request)
        updated_request.update({'user_id':user_id})
        print(updated_request)
        form = CreateEvent(updated_request)
        
        
        if form.is_valid():

            form.save()
            return redirect('event_list')
              # Redirect to event_list page
    else:
        form = CreateEvent()
    return render(request, 'create_event.html', {'form': form, 'isLoggedIn': isLoggedIn, 'loggedInUserName': loggedInUserName})

def getUserId(request):
    user = get_user(request)
    user_id = user.id
    return user_id

def event_list(request):
    isLoggedIn = isUserLoggedIn(request)

    if isLoggedIn:
        loggedInUserName = getLoggedInUserName(request)
    else:
        loggedInUserName = ''
    events = Organiser.objects.filter(user_id=getUserId(request))
    return render(request, 'event_list.html', {'events': events, 'isLoggedIn': isLoggedIn, 'loggedInUserName': loggedInUserName})

def event_details(request):
    eventId = request.GET.get('eventId')
    print('event', eventId)
    
    try:
        eventDetail = Organiser.objects.get(pk=eventId)
        print(eventDetail.event_type)
    except:
        eventDetail = None
        print('EVENT NOT FOUND')
    
    return render(request, 'event_details.html', {'eventDetails':eventDetail})

def homepage(request):
    isLoggedIn = isUserLoggedIn(request)

    if isLoggedIn:
        loggedInUserName = getLoggedInUserName(request)
    else:
        loggedInUserName = ''

    return render(request, 'homepage.html', {'isLoggedIn': isLoggedIn, 'loggedInUserName': loggedInUserName})


def getLoggedInUserName(request):
    user = get_user(request)
    return user.username


def isUserLoggedIn(request):
    user = get_user(request)

    if user.is_authenticated:
        print("Authenticated")
        username = user.username
        print("Authenticated2 = ",user.id)
    else:
        # User is not logged in
        print("not Authenticated")
        username = None
    return username

def event_delete(request):
    eventId = request.GET.get('eventId')
    print('event', eventId)
    try:
        eventDelete = Organiser.objects.get(pk=eventId)
        print(eventDelete.event_type)
        eventDelete.delete()
    except:
        eventDelete = None
        print('EVENT NOT FOUND')
    return redirect('event_list')

def logout_view(request):
    logout(request)
    return redirect('homepage')