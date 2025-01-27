from django import forms
from .models import Booking, BookableService
from django.core.exceptions import ValidationError
from django.utils import timezone

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['checkin_date', 'checkout_date', 'guests']

    checkin_date = forms.DateField(widget=forms.SelectDateWidget())
    checkout_date = forms.DateField(widget=forms.SelectDateWidget())
    guests = forms.IntegerField(min_value=1)

    def clean_checkin_date(self):
        checkin_date = self.cleaned_data.get('checkin_date')
        if checkin_date < timezone.now().date():
            raise ValidationError("Check-in date cannot be in the past.")
        return checkin_date

    def clean_checkout_date(self):
        checkout_date = self.cleaned_data.get('checkout_date')
        if checkout_date < timezone.now().date():
            raise ValidationError("Check-out date cannot be in the past.")

        checkin_date = self.cleaned_data.get('checkin_date')
        if checkout_date <= checkin_date:
            raise ValidationError("Check-out date must be after the check-in" + 
                                  "date.")

        return checkout_date

    def clean_guests(self):
        guests = self.cleaned_data.get('guests')
        if guests < 1:
            raise ValidationError("Number of guests must be at least 1.")
        return guests