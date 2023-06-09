from django.shortcuts import render, redirect

from event.models import Organiser
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
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("HELLO")
    return render(request, 'login.html')
    '''
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("Helo")
            login(request, user)
            return redirect('homepage')  # Redirect to a success page
        else:
            # Authentication failed
            print("Rishu")
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        print("uuuuu")
        return render(request, 'login.html')
    '''
def homepage2(request):
    # Your homepage logic
    return render(request, 'loginhomepage.html')

def create_event(request):
    if request.method == 'POST':
        form = CreateEvent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event-list')
              # Redirect to login page
    else:
        form = CreateEvent()
    return render(request, 'create_event.html', {'form': form})


def homepage(request):
    # Your homepage logic
    return render(request, 'homepage.html')