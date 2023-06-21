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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('catalog/', views.homepage, name='home'),
    path('homepage/', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('register2/', registration_view, name='register2'),
    path('login/', login_view, name='login'),
    path('create_event/', views.create_event, name='create_event'),
    path('event_list/', views.event_list, name='event_list'),
    path('event_details/', views.event_details, name='event_details'),
    path('event_delete/', views.event_delete, name='event_delete'),
    path('logout/', logout_view, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


