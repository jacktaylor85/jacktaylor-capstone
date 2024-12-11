from django.contrib import admin
from .models import BookableService, Booking
# Register your models here.

admin.site.register(BookableService)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'status', 'checkin_date', 'checkout_date', 'total_price')

    def total_price(self, obj):
        return obj.total_price