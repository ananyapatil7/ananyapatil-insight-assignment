from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'Home'),
    path('deleted/', views.deleted, name = 'Article Deleted'),
]