from django.urls import path

from reserv_app import views

urlpatterns = [
    path('reserv/',views.reservdef),
    path('leave/',views.leave),
    path('reserver/',views.reserverdef),
    path('dashbord/',views.dashborddef),
    path('reservdasti/',views.reservdasti),
    path('save_selection/', views.save_selection, name='save_selection'),
    path('new_timereserv/', views.new_timereserv_view, name='new_timereserv_page'),
    path('timeselct/', views.timeselct, name='timeselct'),
    path('summary/', views.summary_view, name='reservation_summary'),
]