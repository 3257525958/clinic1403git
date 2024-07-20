from django.urls import path

from store_app import views

urlpatterns = [
    path('reserv/',views.reservdef),
    ]
