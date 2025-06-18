from django.urls import path
from .views import home, register, book_car

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('book/', book_car, name='book_car'),
]