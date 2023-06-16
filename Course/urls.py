from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.course, name='course'),
    path('<str:slug>', views.coursepost , name ='coursepost'),
] 
