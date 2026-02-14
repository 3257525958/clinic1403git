from django.apps import AppConfig

class SmsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sms_app'

    def ready(self):
        # فقط در صورتی که در محیط اصلی اجرا می‌شیم (نه management commands)
        import os
        if os.environ.get('RUN_MAIN') or not os.environ.get('DJANGO_AUTORELOAD'):
            # جلوگیری از اجرای دوباره در runserver
            from .sms_scheduler import start_scheduler_thread
            start_scheduler_thread()