from django.urls import path

from it_app import views

urlpatterns = [
    path('sendmesaage/',views.sendmesaage),
    path('savemesaage/',views.savemesaage),
    path('control/',views.itcontrol),
    path('controldel/',views.itdeletcontrol),
    ]
