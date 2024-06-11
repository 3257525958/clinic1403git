from django.urls import path

from accountancy_app import views

urlpatterns = [
    path('aghd/',views.aghdgharardad),
    path('laghv/',views.laghvgharardad),
    path('pardakhthoghogh/',views.pardakhthoghogh),
    path('baba/',views.sana),
    ]
