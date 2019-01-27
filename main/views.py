from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Member, Availability, Book
# Create your views here.
from django.http import JsonResponse


def custom_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/user/home')
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
    book_list = Book.objects.all()
    if request.method == 'POST':
        if "submit-book" in request.POST:
            name = request.POST['book-name']
            author_name = request.POST['author-name']
            description = request.POST['description']
            book_image = request.POST['book-image']
            request.user.member.coins = 15.0
            request.user.member.save()
            new_book = Book(owner=request.user.member, name=name, author=author_name, description=description, image=book_image, price=15.0)
            new_book.save()
            return render(request, 'main.html', {'book_list': book_list})
    if request.method == 'POST':
        avail = Availability(address="Arbutus 4750", start_time="12:00", end_time="1:00", days=["Monday", "Tuesday", "Wednesday"], member=request.user.member)
        avail.save()
        return render(request, 'main.html', {'book_list': book_list})
    av_user = Availability.objects.filter(member=request.user.member)
    if not av_user:
        return render(request, 'delivery.html')
    return render(request, 'main.html', {'book_list': book_list})


def buy_book(request):
    book_id = request.GET['book_id']
    book_sold = Book.objects.get(id=book_id)
    if request.user.member.coins >= book_sold.price:
        request.user.member.coins = request.user.member.coins - book_sold.price
        book_sold.being_sold = False
        book_sold.owner = request.user.member
        book_sold.save()
        request.user.member.save()
        return render(request, 'book_sold.html', {'sold': True})
    else:
        return render(request, 'book_sold.html', {'sold': False})


def show_book(request):
    book_id = request.GET['book_id']
    book_info = Book.objects.get(id=book_id)
    return render(request, 'book_info.html', {'book': book_info})


def add_book(request):
    return render(request, 'add_book.html')