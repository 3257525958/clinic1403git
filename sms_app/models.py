from django.db import models
from django.utils import timezone
from cantact_app.models import  accuntmodel # مدل مخاطبان شما

class MessageTemplate(models.Model):
    """قالب پیامک با نام دلخواه"""
    name = models.CharField(max_length=100, unique=True, verbose_name="نام پیام")
    text = models.TextField(verbose_name="متن پیام")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "قالب پیام"
        verbose_name_plural = "قالب‌های پیام"


class SentMessage(models.Model):
    """ثبت پیامک‌های ارسالی"""
    STATUS_CHOICES = (
        ('success', 'موفق'),
        ('failed', 'ناموفق'),
    )
    template = models.ForeignKey(MessageTemplate, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="قالب پیام")
    contact = models.ForeignKey( accuntmodel, on_delete=models.CASCADE, verbose_name="مخاطب")
    message_text = models.TextField(verbose_name="متن ارسالی")
    sent_at = models.DateTimeField(default=timezone.now, verbose_name="زمان ارسال")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='success', verbose_name="وضعیت")
    api_response = models.TextField(blank=True, null=True, verbose_name="پاسخ API")

    def __str__(self):
        return f"{self.contact} - {self.sent_at}"

    class Meta:
        verbose_name = "پیام ارسالی"
        verbose_name_plural = "پیام‌های ارسالی"
        ordering = ['-sent_at']


class ReceivedMessage(models.Model):
    """ثبت پیامک‌های دریافتی"""
    contact = models.ForeignKey( accuntmodel, on_delete=models.CASCADE, verbose_name="مخاطب")
    message_text = models.TextField(verbose_name="متن پیام")
    sender_number = models.CharField(max_length=11, verbose_name="شماره فرستنده")
    received_at = models.DateTimeField(verbose_name="زمان دریافت")
    is_read = models.BooleanField(default=False, verbose_name="خوانده شده؟")
    external_id = models.CharField(max_length=100, blank=True, null=True, unique=True, verbose_name="شناسه پیام در کاوه‌نگار")

    def __str__(self):
        return f"{self.sender_number} - {self.received_at}"

    class Meta:
        verbose_name = "پیام دریافتی"
        verbose_name_plural = "پیام‌های دریافتی"
        ordering = ['-received_at']