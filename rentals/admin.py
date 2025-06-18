from django.contrib import admin
from .models import Car, Booking

class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_day')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date', 'total_price')

admin.site.register(Car, CarAdmin)  
admin.site.register(Booking, BookingAdmin) 