from django import forms
from .models import Booking, BookableService

class BookingForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    booking_date = forms.DateField(widget=forms.SelectDateWidget, label="Booking Date")