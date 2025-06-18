from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Car, Booking
from django import forms

def home(request):
    cars = Car.objects.all()
    return render(request, 'rentals/home.html', {'cars': cars})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "rentals/register.html", {"form": form})

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['car', 'start_date', 'end_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['car'].queryset = Car.objects.all()

@login_required
def book_car(request):
    form = BookingForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        booking = form.save(commit=False)
        if booking.start_date >= booking.end_date:
            form.add_error('end_date', 'End date must be after the start date.')
        else:
            booking.user = request.user
            booking.save()
            return redirect("home")

    return render(request, "rentals/book_car.html", {"form": form})