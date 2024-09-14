from django.urls import path

from it_app import views

urlpatterns = [
    path('sendmesaage/',views.sendmesaage),
    path('tiket/',views.tiketdef),
    path('control/',views.itcontrol),
    path('controldel/',views.itdeletcontrol),
    ]
