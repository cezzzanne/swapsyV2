from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner')
    email = models.EmailField(max_length=150, null=True)
    name = models.CharField(max_length=50, null=True)
    coins = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username