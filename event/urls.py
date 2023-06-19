"""event URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from .views import registration_view
from .views import login_view
from . import views
from django.contrib.auth.views import LoginView
from .views import logout_view
#from .forms import CustomLoginForm

urlpatterns = [
    path('catalog/', views.homepage, name='home'),
    path('homepage/', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('register2/', registration_view, name='register2'),
    #path('login/', LoginView.as_view(authentication_form=CustomLoginForm, template_name='login.html'), name='login'),
    path('login/', login_view, name='login'),
    path('loginhomepage/', views.homepage2, name='loginhomepage'),
    path('create_event/', views.create_event, name='create_event'),
    path('event_list/', views.event_list, name='event_list'),
    path('logout/', logout_view, name='logout'),
]


