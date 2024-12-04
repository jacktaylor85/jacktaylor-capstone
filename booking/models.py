from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class BookableService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Default description")
    location = models.CharField(max_length=200, default="Location")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(null=True, blank=True, default='media/elementor-placeholder-image.webp')
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey('BookableService', on_delete=models.CASCADE)
    booking_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        f'{self.user.username} booked {self.item.name} on {self.booking_date}'