from django.urls import path

from reserv_app import views

urlpatterns = [
    path('reserv/',views.reservdef),
    path('leave/',views.leave),
    path('reserver/',views.reserverdef),
    path('reservdasti/',views.reservdasti),
    path('save_selection/', views.save_selection, name='save_selection'),
    path('new_timereserv/', views.new_timereserv_view, name='new_timereserv_page'),
    path('new_timeleave/', views.new_timeleav_view, name='new_timeleave_name'),
    path('timeselct/', views.timeselct, name='timeselct'),
    # path('timeselctleave/', views.timeselctleave, name='timeselctleave'),
    path('summary/', views.summary_view, name='reservation_summary'),
    path('finalize_leave/', views.finalize_leave, name='finalize_leave'),

    path('dashboard/', views.dashborddef, name='secretary_dashboard'),
    path('search_members/', views.search_members, name='search_members'),
    path('member_profile/', views.member_profile, name='member_profile'),

    path('cashier/', views.cashier_view, name='cashier_view'),
    path('update_advance/', views.update_advance, name='update_advance'),
    path('submit_payment/', views.submit_payment, name='submit_payment'),
    path('start_cashier_session/', views.start_cashier_session, name='start_cashier_session'),

    path('start_reserv_profile/', views.save_reserv_profiles, name='reserv_profile'),

]