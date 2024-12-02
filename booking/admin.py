from django.contrib import admin
from .models import BookableService, Booking
# Register your models here.

admin.site.register(BookableService)
admin.site.register(Booking)