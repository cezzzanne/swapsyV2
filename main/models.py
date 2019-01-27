from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    email = models.EmailField(max_length=150, null=True)
    name = models.CharField(max_length=50, null=True)
    coins = models.IntegerField(default=0)
    rating = models.FloatField(default=3.5)

    def __str__(self):
        return self.user.username


class Availability(models.Model):
    days = ArrayField(models.CharField(max_length=50, blank=True))
    start_time = models.TextField()
    end_time = models.TextField()
    address = models.TextField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='availability', null=True)


class Book(models.Model):
    being_sold = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(upload_to='pic_folder/')
    name = models.TextField()
    author = models.TextField()
    price = models.IntegerField()
    owner = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='books', null=True)
