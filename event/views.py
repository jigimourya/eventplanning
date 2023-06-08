from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


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
        #return render(request, 'login.html')

def homepage(request):
    # Your homepage logic
    return render(request, 'homepage.html')