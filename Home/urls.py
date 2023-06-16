from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/',views.contact , name = 'contact'),
    path('about/',views.about , name = 'about'),
    path('privacy/',views.privacy , name = 'privacy'),

    path('login/', views.login , name = 'login'),
 
]