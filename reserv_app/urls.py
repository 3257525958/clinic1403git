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
    path('new_timeleave/', views.new_timeleav_view, name='new_timeleave_name'),
    path('timeselct/', views.timeselct, name='timeselct'),
    # path('timeselctleave/', views.timeselctleave, name='timeselctleave'),
    path('summary/', views.summary_view, name='reservation_summary'),
    path('finalize_leave/', views.finalize_leave, name='finalize_leave'),
]