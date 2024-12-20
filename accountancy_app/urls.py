from django.urls import path

from accountancy_app import views

urlpatterns = [
    path('aghd/',views.aghdgharardad),
    path('laghv/',views.laghvgharardad),
    path('pardakhthoghogh/',views.pardakhthoghogh),
    path('sana/',views.sana),
    path('ware/',views.warehouse),
    path('froshande/',views.froshande),
    path('anbargardani/',views.anbargardani),
    ]
