from django.urls import path

from cantact_app import views

urlpatterns = [
    path('login/',views.logindef),
    path('addcontact/',views.addcantactdef),
    path('ignor/',views.ignordef),
    ]
