from django.urls import path

from reserv_app import views

urlpatterns = [
    path('reserv/',views.reservdef),
    path('leave/',views.leave),
    path('reserver/',views.reserverdef),
    path('dashbord/',views.dashborddef),
    ]
