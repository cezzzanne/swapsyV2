from django.contrib import admin
from django.urls import path, include
from .views import custom_login, register

urlpatterns = [
    path('', custom_login),
    path('register', register)
]
