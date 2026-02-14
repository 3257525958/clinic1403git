import threading
import time
import schedule
from django.core.wsgi import get_wsgi_application
import os
import django

# تنظیمات جنگو برای اجرای مستقل
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic1403.settings')
django.setup()

from sms_app.views import fetch_incoming_sms
from django.http import HttpRequest


def job():
    """تابعی که هر بار اجرا می‌شه و پیام‌ها رو دریافت می‌کنه"""
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Fetching messages...")
    try:
        request = HttpRequest()
        request.method = 'GET'
        response = fetch_incoming_sms(request)
        print(f"Result: {response.content.decode()}")
    except Exception as e:
        print(f"Error in fetch: {e}")


def run_scheduler():
    """حلقه اصلی زمانبندی"""
    # برنامه‌ریزی برای اجرای job هر ۱ دقیقه
    schedule.every(1).minutes.do(job)

    # اجرای اولیه بلافاصله
    job()

    while True:
        schedule.run_pending()
        time.sleep(1)


def start_scheduler_thread():
    """شروع thread زمانبندی در پس‌زمینه"""
    thread = threading.Thread(target=run_scheduler, daemon=True)
    thread.start()
    print("✅ Scheduler thread started (every 1 minute)")