from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Member
# Create your views here.


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/user/home')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['name']
        user = User.objects.create(username=username)
        email = request.POST['email']
        password = request.POST['password']
        user.set_password(password)
        user.save()
        member = Member(user=user, email=email, name=name)
        member.save()
        if user is not None:
            new_user = authenticate(username=username, password=password)
            login(request, new_user)
            return HttpResponseRedirect('/user/home')
    return render(request, 'register.html')

