from django.contrib import admin
from .models import Member, Availability, Book
# Register your models here.
admin.site.register(Member)
admin.site.register(Availability)
admin.site.register(Book)