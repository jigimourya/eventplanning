from sre_constants import CATEGORY
from tkinter import CURRENT
from typing import Type
from wsgiref.util import request_uri
from django.shortcuts import render, redirect, get_object_or_404
from .models import Organiser, Category, Department
from .forms import CreateEvent, RegistrationForm
from .forms import RegistrationForm2
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth import get_user
from django.contrib.auth import logout
from django.utils import timezone
from datetime import date
import traceback




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
        form = CreateEvent(updated_request, request.FILES)
        
        
        if form.is_valid():

            form.save()
            return redirect('event_list')
              # Redirect to event_list page
    else:
        form = CreateEvent()
        #print(form)

    category = Category.objects.all()

    catList = list()
    for cat in category:
        catName = cat.category_name
        catTuple = (catName, catName)
        catList.append(catTuple)
    print(catList)


    department = Department.objects.all()
    deptList = list()
    for dept in department:
        deptName = dept.department_name
        deptTuple = (deptName, deptName)
        deptList.append(deptTuple)
    print(deptList)

    return render(request, 'create_event.html', {'form': form, 'isLoggedIn': isLoggedIn, 'loggedInUserName': loggedInUserName, 'category': category, 'department': department})

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


def homepage(request):
    isLoggedIn = isUserLoggedIn(request)

    if isLoggedIn:
        loggedInUserName = getLoggedInUserName(request)
    else:
        loggedInUserName = ''

    events =  UpcomingEvents(request)

    return render(request, 'homepage.html', {'isLoggedIn': isLoggedIn, 'loggedInUserName': loggedInUserName, 'upcomingEventsList': events})


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

def event_details(request):
    isLoggedIn = isUserLoggedIn(request)

    if isLoggedIn:
        loggedInUserName = getLoggedInUserName(request)
    else:
        loggedInUserName = ''

    eventId = request.GET.get('eventId')
    print('event', eventId)
    
    try:
        eventDetail = Organiser.objects.get(pk=eventId)
        print(eventDetail.event_type)
    except:
        eventDetail = None
        print('EVENT NOT FOUND')
    
    return render(request, 'event_details.html', {'eventDetails':eventDetail, 'isLoggedIn': isLoggedIn, 'loggedInUserName': loggedInUserName})


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

def event_edit(request):
    eventId = request.GET.get('eventId')
    print('event', eventId)
    
    try:
         if request.method == 'POST':
            print('saved')
            print(request.POST)

            eventDetail = Organiser.objects.get(pk=eventId)
            eventDetail.name_of_event = request.POST.get('event_name')
            eventDetail.venue = request.POST.get('event_location')
            eventDetail.event_date = request.POST.get('event_date')
        
            eventDetail.save()

            return redirect('event_list')

         else:
            print('Keep editing')
            eventEdit = Organiser.objects.get(pk=eventId)
            eventEdit.event_date=eventEdit.event_date.strftime('%Y-%m-%d')
            print(eventEdit.event_type)
            print(eventEdit.event_date)
    except:
        eventEdit = None
        print('EVENT NOT FOUND')
    
    return render(request, 'event_edit.html', {'eventEdit':eventEdit})


def event_save(request):
    if request.method == 'POST':
        print('saved')
        form = CreateEvent(request.POST)
        if form.is_valid():

            form.save()
            return redirect('event_details')
              # Redirect to event_list page
    else:
        form = CreateEvent()
    return render(request, 'event_edit.html', {'form': form})


def UpcomingEvents(request):
   
    #events =  Organiser.objects.order_by('event_date')
    #eventName = Organiser.objects.get(eventDetail = event_details(request))
    #eventType = Organiser.objects.only('event_type')
    #print(events)
    #print(eventType)
    
    print('Event not found')

    now = timezone.now()
    events = Organiser.objects.filter(event_date__gte=now)

    #return render(request, 'homepage.html', {'events': events})

    return events

def category_events(request):
    eventCategory = request.GET.get('category')
    #events = Organiser.objects.filter(event_type=eventCategory)


    today = date.today()
    current_year = today.strftime('%Y')
    print(type(current_year))
    start_year=2000
    end_year = int(current_year) + 10
    print(start_year, end_year)

    years=list()
    for i in range(start_year, end_year+1):
        
        years.append(i)
        
    print(years)   

    eventYear = request.GET.get('eventYear')
    if eventYear == None:
        eventYear = 0
    else:
        eventYear = int(eventYear)
    print('event', eventYear)
    print(Organiser.event_date)

    try:
        if eventYear > 0:
            events = Organiser.objects.filter(event_type=eventCategory, event_date__year=eventYear)
        else:
            events = Organiser.objects.filter(event_type=eventCategory)
        #event_year.event_date
        print(events)
    except Exception as e:
        message = traceback.format_exc()
        print(message)
        events = None
        print('EVENT NOT FOUND')

    return render(request, 'category_events.html', {'events': events, 'eventCategory': eventCategory, 'years': years})

   # return render(request, 'category_events.html', {'events': events, 'today': today, 'current_year': current_year, 'start_year': start_year, 'end_year': end_year, 'years': years, 'event_year': event_year})

def logout_view(request):
    logout(request)
    return redirect('homepage')