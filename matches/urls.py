from django.contrib import admin
from django.urls import path
from . import views

app_name = 'matches'
urlpatterns = [
    path('info/', views.info, name='info'), 
] 