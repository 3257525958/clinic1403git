from django.contrib import admin
from .models import MessageTemplate, SentMessage, ReceivedMessage

@admin.register(MessageTemplate)
class MessageTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'created_at', 'updated_at')
    search_fields = ('name', 'text')

@admin.register(SentMessage)
class SentMessageAdmin(admin.ModelAdmin):
    list_display = ('contact', 'template', 'message_text', 'sent_at', 'status')
    list_filter = ('status', 'template', 'sent_at')
    search_fields = ('contact__firstname', 'contact__lastname', 'contact__phonnumber', 'message_text')
    date_hierarchy = 'sent_at'

@admin.register(ReceivedMessage)
class ReceivedMessageAdmin(admin.ModelAdmin):
    list_display = ('sender_number', 'contact', 'message_text', 'received_at', 'is_read')
    list_filter = ('is_read', 'received_at')
    search_fields = ('sender_number', 'contact__firstname', 'contact__lastname', 'message_text')
    date_hierarchy = 'received_at'