from django.urls import path
from . import views

app_name = 'sms_app'

urlpatterns = [
    path('send/', views.send_sms_view, name='send_sms'),
    path('chat/<int:contact_id>/', views.chat_view, name='chat'),
    path('chats/', views.chat_list_view, name='chat_list'),
    path('fetch-incoming/', views.fetch_incoming_sms, name='fetch_incoming'),
    path('ajax/new-messages/<int:contact_id>/', views.ajax_get_new_messages, name='ajax_new_messages'),
    path('api/not-received/', views.get_not_received_contacts, name='not_received'),
]