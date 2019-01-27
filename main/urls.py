from django.contrib import admin
from django.urls import path, include
from .views import custom_login, register, home, buy_book, show_book, add_book

urlpatterns = [
    path('', custom_login),
    path('register', register),
    path('user/home', home),
    path('user/buy/book', buy_book),
    path('user/show/book', show_book),
    path('user/add-book', add_book)
]
