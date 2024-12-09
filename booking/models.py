from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class BookableService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Default description")
    location = models.CharField(max_length=200, default="Location")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(null=True, blank=True, upload_to='static/images')
    availability = models.BooleanField(default=True)
    

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    service = models.CharField(max_length=255, default="Default service")
    booking_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[("Pending", "Pending"), ("Confirmed", "Confirmed")], default="Default status")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service} - {self.status}"