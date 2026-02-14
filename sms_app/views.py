import json
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from kavenegar import KavenegarAPI, APIException, HTTPException
import requests

# مدل مخاطبان شما (با املای دقیق)
from cantact_app.models import accuntmodel

from .models import MessageTemplate, SentMessage, ReceivedMessage


# ======================
# تنظیمات کاوه‌نگار
KAVENEGAR_API_KEY = '527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D'
KAVENEGAR_SENDER = '9982003178'
# ======================


def replace_placeholders(text, contact):
    """
    جایگزینی {firstname} و {lastname} با مقادیر واقعی مخاطب
    """
    replacements = {
        '{firstname}': contact.firstname or '',
        '{lastname}': contact.lastname or '',
        '{name}': f"{contact.firstname} {contact.lastname}".strip() or '',
    }
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text


def send_sms_view(request):
    """
    صفحه اصلی ارسال پیام: لیست مخاطبان با چک‌باکس، انتخاب قالب و نوشتن پیام جدید
    """
    contacts = accuntmodel.objects.all()
    templates = MessageTemplate.objects.all()

    if request.method == 'POST':
        message_text = request.POST.get('message_text')
        message_name = request.POST.get('message_name')
        contact_ids = request.POST.getlist('contacts')

        if not message_text:
            messages.error(request, "متن پیام نمی‌تواند خالی باشد.")
            return redirect('sms_app:send_sms')

        if not contact_ids:
            messages.error(request, "حداقل یک مخاطب را انتخاب کنید.")
            return redirect('sms_app:send_sms')

        # ایجاد یا بازیابی قالب پیام
        template = None
        if message_name:
            template, _ = MessageTemplate.objects.get_or_create(name=message_name, defaults={'text': message_text})

        api = KavenegarAPI(KAVENEGAR_API_KEY)
        success_count = 0
        fail_count = 0

        for contact_id in contact_ids:
            try:
                contact = accuntmodel.objects.get(pk=contact_id)
                # جایگزینی placeholders در متن پیام
                personalized_text = replace_placeholders(message_text, contact)

                params = {
                    'sender': KAVENEGAR_SENDER,
                    'receptor': contact.phonnumber,
                    'message': personalized_text,
                }
                response = api.sms_send(params)
                SentMessage.objects.create(
                    template=template,
                    contact=contact,
                    message_text=personalized_text,  # ذخیره متن نهایی
                    status='success',
                    api_response=json.dumps(response)
                )
                success_count += 1
            except accuntmodel.DoesNotExist:
                fail_count += 1
            except (APIException, HTTPException) as e:
                SentMessage.objects.create(
                    template=template,
                    contact=contact if 'contact' in locals() else None,
                    message_text=message_text,
                    status='failed',
                    api_response=str(e)
                )
                fail_count += 1
            except Exception as e:
                fail_count += 1

        messages.success(request, f"پیامک با موفقیت برای {success_count} مخاطب ارسال شد. {fail_count} ناموفق.")
        return redirect('sms_app:send_sms')

    # ساخت گزینه‌های چک‌باکس
    contact_choices = [(c.id, f"{c.firstname} {c.lastname} - {c.phonnumber}") for c in contacts]

    context = {
        'contacts': contacts,
        'templates': templates,
        'contact_choices': contact_choices,
    }
    return render(request, 'sms_app/send_sms.html', context)


def chat_view(request, contact_id):
    """
    صفحه چت با یک مخاطب خاص
    """
    contact = get_object_or_404(accuntmodel, pk=contact_id)

    # دریافت پیام‌های ارسالی و دریافتی
    sent_messages = SentMessage.objects.filter(contact=contact).values('message_text', 'sent_at')
    received_messages = ReceivedMessage.objects.filter(contact=contact).values('message_text', 'received_at')

    messages_list = []
    for msg in sent_messages:
        messages_list.append({
            'text': msg['message_text'],
            'time': msg['sent_at'],
            'direction': 'outgoing'
        })
    for msg in received_messages:
        messages_list.append({
            'text': msg['message_text'],
            'time': msg['received_at'],
            'direction': 'incoming'
        })
    messages_list.sort(key=lambda x: x['time'])

    # علامت‌گذاری پیام‌های دریافتی به عنوان خوانده شده
    ReceivedMessage.objects.filter(contact=contact, is_read=False).update(is_read=True)

    if request.method == 'POST':
        reply_text = request.POST.get('reply_text')
        if reply_text:
            try:
                # جایگزینی placeholders در پاسخ (در صورت نیاز)
                personalized_reply = replace_placeholders(reply_text, contact)

                api = KavenegarAPI(KAVENEGAR_API_KEY)
                params = {
                    'sender': KAVENEGAR_SENDER,
                    'receptor': contact.phonnumber,
                    'message': personalized_reply,
                }
                response = api.sms_send(params)
                SentMessage.objects.create(
                    template=None,
                    contact=contact,
                    message_text=personalized_reply,
                    status='success',
                    api_response=json.dumps(response)
                )
                messages.success(request, "پاسخ ارسال شد.")
            except (APIException, HTTPException) as e:
                messages.error(request, f"خطا در ارسال: {e}")
        return redirect('sms_app:chat', contact_id=contact.id)

    context = {
        'contact': contact,
        'messages': messages_list,
    }
    return render(request, 'sms_app/chat.html', context)


def chat_list_view(request):
    """
    نمایش لیست همه مخاطبان با آخرین پیام (ارسالی یا دریافتی) و زمان آن
    """
    contacts = accuntmodel.objects.all().order_by('firstname')
    chat_list = []

    for contact in contacts:
        last_sent = SentMessage.objects.filter(contact=contact).order_by('-sent_at').first()
        last_received = ReceivedMessage.objects.filter(contact=contact).order_by('-received_at').first()

        last_message = None
        last_time = None
        if last_sent and last_received:
            if last_sent.sent_at > last_received.received_at:
                last_message = last_sent
                last_time = last_sent.sent_at
            else:
                last_message = last_received
                last_time = last_received.received_at
        elif last_sent:
            last_message = last_sent
            last_time = last_sent.sent_at
        elif last_received:
            last_message = last_received
            last_time = last_received.received_at

        chat_list.append({
            'contact': contact,
            'last_message': last_message.message_text if last_message else 'هنوز پیامی وجود ندارد',
            'last_time': last_time,
            'last_direction': 'outgoing' if isinstance(last_message, SentMessage) else 'incoming' if last_message else None,
        })

    # ایجاد یک زمان بسیار قدیمی و region-aware برای مقایسه
    very_old = timezone.make_aware(datetime.datetime(1900, 1, 1), timezone.get_current_timezone())

    # مرتب‌سازی بر اساس آخرین زمان (جدیدترین در بالا)
    chat_list.sort(key=lambda x: x['last_time'] if x['last_time'] else very_old, reverse=True)

    context = {
        'chat_list': chat_list,
    }
    return render(request, 'sms_app/chats.html', context)


def fetch_incoming_sms(request):
    """
    دریافت پیامک‌های جدید از کاوه‌نگار و ذخیره در پایگاه داده
    این ویو می‌تواند توسط Cron یا مدیریت دستی فراخوانی شود.
    """
    try:
        url = f"https://api.kavenegar.com/v1/{KAVENEGAR_API_KEY}/sms/receive.json"
        params = {
            'linenumber': KAVENEGAR_SENDER,
            'isread': 0
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if data['result'] is not None and 'entries' in data['result']:
            for entry in data['result']['entries']:
                message = entry['message']
                sender = entry['sender']
                date = entry['date']
                message_id = entry.get('messageid', None)

                if message_id and ReceivedMessage.objects.filter(external_id=message_id).exists():
                    continue

                try:
                    contact = accuntmodel.objects.get(phonnumber=sender)
                except accuntmodel.DoesNotExist:
                    contact = None

                ReceivedMessage.objects.create(
                    contact=contact,
                    message_text=message,
                    sender_number=sender,
                    received_at=timezone.datetime.fromtimestamp(int(date)),
                    is_read=False,
                    external_id=message_id
                )
        return JsonResponse({'status': 'ok', 'detail': 'پیام‌های جدید دریافت شدند.'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'detail': str(e)})


@csrf_exempt
def ajax_get_new_messages(request, contact_id):
    """
    دریافت تمام پیام‌های یک مخاطب (برای بروزرسانی خودکار صفحه چت)
    """
    if request.method == 'GET':
        contact = get_object_or_404(accuntmodel, pk=contact_id)
        sent = SentMessage.objects.filter(contact=contact).values('message_text', 'sent_at')
        received = ReceivedMessage.objects.filter(contact=contact).values('message_text', 'received_at')

        ReceivedMessage.objects.filter(contact=contact, is_read=False).update(is_read=True)

        messages_list = []
        for msg in sent:
            messages_list.append({
                'text': msg['message_text'],
                'time': msg['sent_at'].isoformat(),
                'direction': 'outgoing'
            })
        for msg in received:
            messages_list.append({
                'text': msg['message_text'],
                'time': msg['received_at'].isoformat(),
                'direction': 'incoming'
            })
        messages_list.sort(key=lambda x: x['time'])
        return JsonResponse(messages_list, safe=False)
    return JsonResponse({'error': 'method not allowed'}, status=405)


def get_not_received_contacts(request):
    """
    برگرداندن لیست شناسه مخاطبانی که پیام با نام مشخص را دریافت نکرده‌اند
    """
    message_name = request.GET.get('message_name')
    if not message_name:
        return JsonResponse({'error': 'message_name required'}, status=400)
    try:
        template = MessageTemplate.objects.get(name=message_name)
    except MessageTemplate.DoesNotExist:
        return JsonResponse({'error': 'قالب یافت نشد'}, status=404)

    all_contacts = set(accuntmodel.objects.values_list('id', flat=True))
    received_contacts = set(SentMessage.objects.filter(template=template, status='success').values_list('contact_id', flat=True))
    not_received = list(all_contacts - received_contacts)
    return JsonResponse({'contact_ids': not_received})