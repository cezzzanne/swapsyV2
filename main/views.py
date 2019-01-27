from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Member, Availability
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


def home(request):
    if request.method == 'POST':
        avail = Availability(address="Arbutus 4750", start_time="12:00", end_time="1:00", days=["Monday", "Tuesday", "Wednesday"], member=request.user.member)
        avail.save()
        return render(request, 'e.html')
    av_user = Availability.objects.filter(member=request.user.member)
    if not av_user:
        return render(request, 'delivery.html')
    return render(request, 'main.html')


def buy_book(request):
    price = request.POST['price']
    book_id = request.POST['book_id']
    if request.user.member.coins >= int(price):
        request.user.member.coins = request.user.member.coins - int(price)
        request.user.member.coins.save()
        return # confirmation
    else:
        return # error

