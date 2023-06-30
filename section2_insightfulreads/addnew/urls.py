from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'Home'),
    path('added/', views.added, name = 'Article Added!'),
]