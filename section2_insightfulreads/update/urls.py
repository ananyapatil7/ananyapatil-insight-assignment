from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'Home'),
    path('updated/', views.updated, name = 'Article Updated!'),
    path('details/', views.details, name = 'Update Article'),
]