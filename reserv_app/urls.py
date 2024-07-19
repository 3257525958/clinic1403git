from django.urls import path

from reserv_app import views

urlpatterns = [
    path('sabt/',views.reservdef),
    path('leave/',views.leave),
    path('reservtion/',views.reserverdef),
    path('dashbord/',views.dashborddef),
    path('reservdasti/',views.reservdasti),
    ]
