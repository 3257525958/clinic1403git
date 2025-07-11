from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from cantact_app.views import dateset,stry,strd,strb
from jobs_app.models import *
from jalali_date import date2jalali,datetime2jalali
import matplotlib
from reserv_app.models import *
from kavenegar import *
import random
from datetime import datetime as dt
from datetime import timedelta
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from cantact_app.models import accuntmodel
from reserv_app.models import fpeseshktestmodel
from cash_app.models import bankmodel , castmodel
from num2words import num2words
import json
import jdatetime
from django.core.serializers import serialize
from django.db.models import Q
from it_app.views import sendmessage
from django.contrib.auth import authenticate,login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


ww = ['t']
shamsiarray = ['t']
miladiarray = ['t']
selectprocedure = ['t']
reservetebar = ['t']
day = ['t']
day.clear()
level = ['']
loginetebar = ['t']
reservposition = ['0']
file_botax = ["0"]
for i  in range(10) :
    file_botax.append("0")
mellicoduser = ["0"]
matplotlib.use('Agg')
def strb(tdef):
    x = str(datetime2jalali(tdef).strftime('%a %d %b %y'))
    rmonth = x[7:10]
    ag_month = rmonth
    if ag_month == 'Far':
        ag_month = 'فروردین'
    if ag_month == 'Ord':
        ag_month = 'اردیبهشت'
    if ag_month == 'Kho':
        ag_month = 'خرداد'
    if ag_month == 'Tir':
        ag_month = 'تیر'
    if ag_month == 'Mor':
        ag_month = 'مرداد'
    if ag_month == 'Sha':
        ag_month = 'شهریور'
    if ag_month == 'Meh':
        ag_month = 'مهر'
    if ag_month == 'Aba':
        ag_month = 'آبان'
    if ag_month == 'Aza':
        ag_month = 'آذر'
    if ag_month == 'Dey':
        ag_month = 'دی'
    if ag_month == 'Bah':
        ag_month = 'بهمن'
    if ag_month == 'Esf':
        ag_month = 'اسفند'
    rmonth = ag_month
    return (rmonth)
def strbadd(tdef):
    x = str(datetime2jalali(tdef).strftime('%a %d %b %y'))
    rmonth = x[7:10]
    ag_month = rmonth
    if ag_month == 'Far':
        ag_month = '01'
    if ag_month == 'Ord':
        ag_month = '02'
    if ag_month == 'Kho':
        ag_month = '03'
    if ag_month == 'Tir':
        ag_month = '04'
    if ag_month == 'Mor':
        ag_month = '05'
    if ag_month == 'Sha':
        ag_month = '06'
    if ag_month == 'Meh':
        ag_month = '07'
    if ag_month == 'Aba':
        ag_month = '08'
    if ag_month == 'Aza':
        ag_month = '09'
    if ag_month == 'Dey':
        ag_month = '10'
    if ag_month == 'Bah':
        ag_month = '11'
    if ag_month == 'Esf':
        ag_month = '12'
    rmonth = ag_month
    return (rmonth)
def strd(tdef):
    x = str(datetime2jalali(tdef).strftime('%a %d %b %y'))
    rday = x[4:6]
    if rday == '01':
        rday = '1'
    if rday == '02':
        rday = '2'
    if rday == '03':
        rday = '3'
    if rday == '04':
        rday = '4'
    if rday == '05':
        rday = '5'
    if rday == '06':
        rday = '6'
    if rday == '07':
        rday = '7'
    if rday == '08':
        rday = '8'
    if rday == '09':
        rday = '9'
    return (rday)
def stra(tdef):
    x = str(datetime2jalali(tdef).strftime('%a %d %b %y'))
    rweek = x[0:3]
    if rweek == 'Sat':
        rweek = 'شنبه'
    if rweek == 'Sun':
        rweek = 'یکشنبه'
    if rweek == 'Mon':
        rweek = 'دوشنبه'
    if rweek == 'Tue':
        rweek = 'سه‌شنبه'
    if rweek == 'Wed':
        rweek = 'چهارشنبه'
    if rweek == 'Thu':
        rweek = 'پنج‌شنبه'
    if rweek == 'Fri':
        rweek = 'جمعه'
    return (rweek)
def stry(tdef):
    x = str(datetime2jalali(tdef).strftime('%a %d %b %y'))
    ryear = x[11:]
    return (ryear)
def stradb(tdef):
    r = stra(tdef)+' '+strd(tdef)+' '+strb(tdef)
    return (r)
def stradby(tdef):
    r = stra(tdef)+' '+strd(tdef)+' '+strb(tdef)+' '+stry(tdef)
    return (r)
def convert_english_to_persian(number):
    translation_dict = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹'
    }
    num_str = str(number)
    return ''.join([translation_dict.get(c, c) for c in num_str])
def summary_view(request: HttpRequest) -> HttpResponse:
    # مثال: خواندن داده‌های ذخیره‌شده در سشن
    s = request.session.get('selected_service_id')
    procedureselect = request.session.get('selected_option_id')
    melicod = request.session.get('national_code')
    selected_day = request.session.get('selected_day')
    selected_time = request.session.get('selected_time')
    select_day_date = dt.now()
    try:
        select_day_date += timedelta(days= int(selected_day) + 1)
    except:
        a=1
    request.session['dateshamsireserv'] = stradb(select_day_date)
    request.session['datemiladireserv'] = select_day_date.strftime('%a %d %b %y')
    request.session['yearshamsi'] = stry(dt.now())
    request.session['numbertime'] = selected_time

    selectprocedure.append(stradb(select_day_date))
    selectprocedure.append(select_day_date.strftime('%a %d %b %y'))
    selectprocedure.append(stry(dt.now()))
    selectprocedure.append(selected_time)
    s = ""
    if selected_time == 1:
        s = "10"
        selectprocedure.append("10:00")
    if selected_time == 2:
        s = "10:15"
        selectprocedure.append("10:15")
    if selected_time == 3:
        s = "10:30"
        selectprocedure.append("10:30")
    if selected_time == 4:
        s = "10:45"
        selectprocedure.append("10:45")
    if selected_time == 5:
        s = "11"
        selectprocedure.append("11:00")
    if selected_time == 6:
        s = "11:15"
        selectprocedure.append("11:15")
    if selected_time == 7:
        s = "11:30"
        selectprocedure.append("11:30")
    if selected_time == 8:
        s = "11:45"
        selectprocedure.append("11:5")
    if selected_time == 9:
        s = "12"
        selectprocedure.append("12:00")
    if selected_time == 10:
        s = "12:15"
        selectprocedure.append("12:15")
    if selected_time == 11:
        s = "12:30"
        selectprocedure.append("12:30")
    if selected_time == 12:
        s = "12:45"
        selectprocedure.append("12:45")
    if selected_time == 13:
        s = "13"
        selectprocedure.append("13:00")
    if selected_time == 14:
        s = "13:15"
        selectprocedure.append("13:15")
    if selected_time == 15:
        s = "13:30"
        selectprocedure.append("13:30")
    if selected_time == 16:
        s = "13:45"
        selectprocedure.append("13:45")
    if selected_time == 17:
        s = "14"
        selectprocedure.append("14:00")
    if selected_time == 18:
        s = "14:15"
        selectprocedure.append("14:15")
    if selected_time == 19:
        s = "14:30"
        selectprocedure.append("14:30")
    if selected_time == 20:
        s = "14:45"
        selectprocedure.append("14:45")
    if selected_time == 21:
        s = "15"
        selectprocedure.append("15:00")
    if selected_time == 22:
        s = "15:15"
        selectprocedure.append("15:15")
    if selected_time == 23:
        s = "15:30"
        selectprocedure.append("15:30")
    if selected_time == 24:
        s = "15:45"
        selectprocedure.append("15:45")
    if selected_time == 25:
        s = "16"
        selectprocedure.append("16:00")
    if selected_time == 26:
        s = "16:15"
        selectprocedure.append("16:15")
    if selected_time == 27:
        s = "16:30"
        selectprocedure.append("16:30")
    if selected_time == 28:
        s = "16:45"
        selectprocedure.append("16:45")
    if selected_time == 29:
        s = "17"
        selectprocedure.append("17:00")
    if selected_time == 30:
        s = "17:15"
        selectprocedure.append("17:15")
    if selected_time == 31:
        s = "17:30"
        selectprocedure.append("17:30")
    if selected_time == 32:
        s = "17:45"
        selectprocedure.append("17:45")
    if selected_time == 33:
        s = "18"
        selectprocedure.append("18:00")
    if selected_time == 34:
        s = "18:15"
        selectprocedure.append("18:15")
    if selected_time == 35:
        s = "18:30"
        selectprocedure.append("18:30")
    if selected_time == 36:
        s = "18:45"
        selectprocedure.append("18:45")
    if selected_time == 37:
        s = "19"
        selectprocedure.append("19:00")
    if selected_time == 38:
        s = "19:15"
        selectprocedure.append("19:15")
    if selected_time == 39:
        s = "19:30"
        selectprocedure.append("19:30")
    if selected_time == 40:
        s = "19:45"
        selectprocedure.append("19:45")
    request.session['hourreserv'] = s
    works = workmodel.objects.all()
    banks = bankmodel.objects.all()
    context = {'l':'l'}
    for work in works:
        if int(work.id) == int(procedureselect) :
            context = {
            'work' : work.work,
            'detalework' : work.detalework,
            'personwork' : work.person,
            'dateshamsi' : stradb(select_day_date),
            'hoursreserv' : s,
            'banks':banks,

            }
    j = ''
    d = ''
    p = ''
    t = ''
    c = ''
    f = ''
    ll = ''
    p = ''
    v = ''

    for work in works:
        if work.id == int(procedureselect) :
            j = work.work
            d = work.detalework
            p = work.melicodpersonel
            c = work.cast
            v = work.vahed
            if work.time == "زمان کمی میبرد":
                t = "0"
                selectprocedure.append("0")
            if work.time == "پانزده دقیقه":
                t = "1"
                selectprocedure.append("1")
            if work.time == "سی دقیقه":
                t = "2"
                selectprocedure.append("2")
            if work.time == "چهل و پنج دقیقه":
                t = "3"
                selectprocedure.append("3")
            if work.time == "یک ساعت":
                t = "4"
                selectprocedure.append("4")
            if work.time == "یک ساعت و پانزده دقیقه":
                t = "5"
                selectprocedure.append("5")
            if work.time == "یک ساعت و نیم":
                t = "6"

    users = accuntmodel.objects.all()
    for user in users:
        if int(user.melicode) == int(request.session['national_code']):
            f = user.firstname
            ll = user.lastname
            ph = user.phonnumber


    reservemodeltest.objects.create(
        mellicode = request.session['national_code'],
        jobreserv = j,
        detalereserv = d,
        personreserv = p,
        timereserv = t,
        castreserv = c,
        numbertime = request.session['selected_time'],
        hourreserv = request.session['hourreserv'],
        dateshamsireserv = stradb(select_day_date),
        datemiladireserv = select_day_date.strftime('%a %d %b %y'),
        yearshamsi = stry(select_day_date),
        phonnumber = ph,
        fiestname = f,
        lastname = ll,
        vahed = v,
        idwork = str(procedureselect)
        # bankpeyment = models.CharField(max_length=200, default='-3',null=True)
    )
    if request.session.get('recive-of') == 'profile':
        return render(request, 'reserv_end_profile.html', context)
    return render(request, 'new_reserv_end.html', context)

@csrf_exempt  # در محیط تولید از توکن CSRF استفاده کنید
def timeselct(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            selected_day = data.get('day')
            selected_time = data.get('time')
            request.session['selected_day'] = selected_day
            request.session['selected_time'] = selected_time
            # هر عملیات دلخواه دیگر...
            # ارسال آدرس صفحه HTML بعدی
            return JsonResponse({
                'redirect_url': reverse('reservation_summary')
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
@csrf_exempt
# در محیط تولیدی پیشنهاد می‌شود مدیریت CSRF به روش امن‌تر انجام شود.
def save_selection(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            service_id = data.get('service')
            option_id = data.get('option')
            national_code = data.get('nationalcode')
            try:
                workselectid = int(option_id.split('+')[0])
            except Exception as e:
                workselectid = "None"

            # ذخیره اطلاعات در session به نحوی که در ادامه بتوانید از آن‌ها استفاده کنید
            request.session['selected_service_id'] = service_id
            request.session['selected_option_id'] = workselectid
            request.session['national_code'] = national_code

            # ارسال URL صفحه new_timereserv به کلاینت
            return JsonResponse({
                'redirect_url': reverse('new_timereserv_page')  # نام URL صفحه جدید
            })
        except Exception as e:
            print("Error:", e)
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)
def convert(t):
    y = convert_english_to_persian(stry(t))
    m = convert_english_to_persian(strbadd(t))
    d = convert_english_to_persian(strd(t))
    return (y+'/'+m+'/'+d)
# فرض کنید توابع convert و timebefor در فایل utils یا ماژول مربوطه موجود باشند.
# از مثال‌های زیر استفاده کنید:
# from .utils import convert, timebefor

@csrf_exempt
def new_timereserv_view(request):
    print(22)
    # دریافت داده انتخاب شده از session (مثلاً شماره خدمت و سایر اطلاعات)
    s = request.session.get('selected_service_id')
    procedureselect = request.session.get('selected_option_id')
    melicod = request.session.get('national_code')

    if request.method == 'POST':
        try:
            # دریافت داده‌های ارسالی به صورت JSON
            data = json.loads(request.body.decode('utf-8'))
            selected_date = data.get('selected_date')
            selected_time = data.get('datetime')
            try:
                workselectid = procedureselect
            except Exception as e:
                workselectid = "None"

            # دریافت زمان‌های رزرو شده با استفاده از تابع timebefor
            ws = workmodel.objects.all()
            melicod = 0
            for w in ws:
                if int(w.id) == int(workselectid):
                    melicod = int(w.melicodpersonel)
            reserved_times = timebefor(selected_date, workselectid, melicod)
            return JsonResponse({'reserved_times': reserved_times})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    else:  # حالت GET
        default_date = dt.now() + timedelta(days=2)
        jalali_date = convert(default_date)

        # حذف داده از session پس از استفاده
        # if 'procedureselect' in request.session:
        #     del request.session['procedureselect']

        try:
            workselectid = int(procedureselect.split('+')[0])
        except Exception as e:
            workselectid = "None"

        reserved_times = timebefor('1', workselectid, melicod)
        reserved_times_json = json.dumps(reserved_times)

        # آماده‌سازی context برای ارسال به قالب HTML
        context = {
            'workselectid': workselectid,
            'melicode': request.user.username,
            'reserved_times_json': reserved_times_json,
        }
        return render(request, 'new_timereserv.html', context)

def timebefor(namberdate, workselectid,melicode):
    # works = workmodel.objects.all()
    # c = 0
    # personelmelicode = '0'
    # berand = ''
    if workselectid != "None":
        reservmovaghats = reservemodeltest.objects.all()
        # ___________در این قسمت تعداد روزهایی که قرار هستش به مراجعه کننده نشون بدیم مشخص میشه____
        # __________آرایه shmsiarray_ساخته میشه به تعداد tedaderooz  به ترتیب از امروز روز میچینه تو خودش________
        t = dt.now()
        t += timedelta(days=1+int(namberdate))
        # ____________در آرایه ی dayarr  بیست تا true مسازه که برای هر روز نشانه ازاد بودن بیست تایم ده صبح تا 8 شب هستش________
        # _________بعد میاد محدودیتها رو اعمال میکنه و هذ تایم رو براساس محدودتها ممکنه false کنه یا true نگه داره_________
        dayarr = ['t']
        dayarr.clear()
        dayarr.append(stradb(t))
        for h in range(40):
            dayarr.append('true')

        # _____برسی مرخصی ها و حضور اپراتوری که انتخاب شده_________
#         ss = [1]
#         ss.clear()
#         ls = leavemodel.objects.all()
#         for l in ls:
#             if int(l.personelmelicod) == int(melicode):
#                 if int(l.date) == int(stry(t) + strbadd(t) + strd(t)):
#                     s = l.leave.split(",")
#                     for i in s:
#                         b = int(i)+1
#                         ss.append(int(b))
#         for i in ss :
#             dayarr[i] = 'false'
#         # ---------وقتی یه نفر یه کاری رو انتخاب میکنه تا قبل از پرداخت براش رزرو میشه تا کس دیگه ای تو این فاصله نتونه رزروش کنه--------
#         # for reservmovaghat in reservmovaghats:
#         #     if int(reservmovaghat.personreserv) == int(melicode):
#         #         if reservmovaghat.dateshamsireserv == stradb(t):
#         #             if reservmovaghat.timereserv == '1':
#         #                 dayarr[int(reservmovaghat.numbertime)] = "false"
#         #             if reservmovaghat.timereserv == '2':
#         #                 dayarr[int(reservmovaghat.numbertime)] = "false"
#         #                 dayarr[int(reservmovaghat.numbertime) + 1] = "false"
#         #             if reservmovaghat.timereserv == '3':
#         #                 dayarr[int(reservmovaghat.numbertime)] = "false"
#         #                 dayarr[int(reservmovaghat.numbertime) + 1] = "false"
#         #                 dayarr[int(reservmovaghat.numbertime) + 2] = "false"
#         #             if reservmovaghat.timereserv == '4':
#         #                 dayarr[int(reservmovaghat.numbertime)] = "false"
#         #                 dayarr[int(reservmovaghat.numbertime) + 1] = "false"
#         #                 dayarr[int(reservmovaghat.numbertime) + 2] = "false"
#         #                 dayarr[int(reservmovaghat.numbertime) + 3] = "false"
#         #             if reservmovaghat.timereserv == '5':
#         #                 dayarr[int(reservmovaghat.numbertime)] = "false"
#         #                 dayarr[int(reservmovaghat.numbertime) + 1] = "false"
#         #                 dayarr[int(reservmovaghat.numbertime) + 2] = "false"
#         #                 dayarr[int(reservmovaghat.numbertime) + 3] = "false"
#         #                 dayarr[int(reservmovaghat.numbertime) + 4] = "false"
#         #             if reservmovaghat.timereserv == '6':
#         #                 dayarr[int(reservmovaghat.numbertime)] = "false"
#         #                 dayarr[int(reservmovaghat.numbertime) + 1] = "false"
#         #                 dayarr[int(reservmovaghat.numbertime) + 2] = "false"
#         #                 dayarr[int(reservmovaghat.numbertime) + 3] = "false"
#         #                 dayarr[int(reservmovaghat.numbertime) + 4] = "false"
#         #                 dayarr[int(reservmovaghat.numbertime) + 5] = "false"
#
#
# # -------------------------اینجا رزرو های قبلی رو چک میکنه---------
#
#         res = reservemodel.objects.all()
#         for r in res:
#             if int(r.personreserv) == int(melicode):
#                 if r.dateshamsireserv == stradb(t):
#                     if r.timereserv == '1':
#                         dayarr[int(r.numbertime)] = "false"
#                     if r.timereserv == '2':
#                         dayarr[int(r.numbertime)] = "false"
#                         dayarr[int(r.numbertime) + 1] = "false"
#                     if r.timereserv == '3':
#                         dayarr[int(r.numbertime)] = "false"
#                         dayarr[int(r.numbertime) + 1] = "false"
#                         dayarr[int(r.numbertime) + 2] = "false"
#                     if r.timereserv == '4':
#                         dayarr[int(r.numbertime)] = "false"
#                         dayarr[int(r.numbertime) + 1] = "false"
#                         dayarr[int(r.numbertime) + 2] = "false"
#                         dayarr[int(r.numbertime) + 3] = "false"
#                     if r.timereserv == '5':
#                         dayarr[int(r.numbertime)] = "false"
#                         dayarr[int(r.numbertime) + 1] = "false"
#                         dayarr[int(r.numbertime) + 2] = "false"
#                         dayarr[int(r.numbertime) + 3] = "false"
#                         dayarr[int(r.numbertime) + 4] = "false"
#                     if r.timereserv == '6':
#                         dayarr[int(r.numbertime)] = "false"
#                         dayarr[int(r.numbertime) + 1] = "false"
#                         dayarr[int(r.numbertime) + 2] = "false"
#                         dayarr[int(r.numbertime) + 3] = "false"
#                         dayarr[int(r.numbertime) + 4] = "false"
#                         dayarr[int(r.numbertime) + 5] = "false"
# ----------------------------------------------------------------------------------------------------------------------------------


# # ---------------------------------------------اگر کاری مه انتخاب شده بیش از15دقیقه باشه یعنی دو تا 15 دقیقه یا سه  یا پهارتا یا پنج تا 15 دقیقه باشه-----------
# # ------باید چک شود که تا تایم های اینده اش  به همون اندازه که وقت میخواد وقت باشه ---------------------------------------
        #
        ws = workmodel.objects.all()

        sel = ''
        for f in ws:
            if int(workselectid) == int(f.id):
                if f.time == "زمان کمی میبرد":
                    sel = "0"
                if f.time == "پانزده دقیقه":
                    sel = "1"
                if f.time == "سی دقیقه":
                    sel = "2"
                if f.time == "چهل و پنج دقیقه":
                    sel = "3"
                if f.time == "یک ساعت":
                    sel = "4"
                if f.time == "یک ساعت و پانزده دقیقه":
                    sel = "5"
                if f.time == "یک ساعت و نیم":
                    sel = "6"

        #
        if sel == "2":
            for hh in range(39):
                hh += 1
                if dayarr[int(hh) + 1] == "false":
                    dayarr[int(hh)] = "false"
            dayarr[40] = "false"
        if sel == "3":
            for hh in range(38):
                hh += 1
                if dayarr[int(hh) + 1] == "false":
                    dayarr[int(hh)] = "false"
                if dayarr[int(hh) + 2] == "false":
                    dayarr[int(hh)] = "false"
            dayarr[39] = "false"
            dayarr[40] = "false"
        if sel == "4":
            for hh in range(37):
                hh += 1
                if dayarr[int(hh) + 1] == "false":
                    dayarr[int(hh)] = "false"
                if dayarr[int(hh) + 2] == "false":
                    dayarr[int(hh)] = "false"
                if dayarr[int(hh) + 3] == "false":
                    dayarr[int(hh)] = "false"
            dayarr[38] = "false"
            dayarr[39] = "false"
            dayarr[40] = "false"
        if sel == "5":
            for hh in range(36):
                hh += 1
                if dayarr[int(hh) + 1] == "false":
                    dayarr[int(hh)] = "false"
                if dayarr[int(hh) + 2] == "false":
                    dayarr[int(hh)] = "false"
                if dayarr[int(hh) + 3] == "false":
                    dayarr[int(hh)] = "false"
                if dayarr[int(hh) + 4] == "false":
                    dayarr[int(hh)] = "false"
            dayarr[37] = "false"
            dayarr[38] = "false"
            dayarr[39] = "false"
            dayarr[40] = "false"
        if sel == "6":
            for hh in range(35):
                hh += 1
                if dayarr[int(hh) + 1] == "false":
                    dayarr[int(hh)] = "false"
                if dayarr[int(hh) + 2] == "false":
                    dayarr[int(hh)] = "false"
                if dayarr[int(hh) + 3] == "false":
                    dayarr[int(hh)] = "false"
                if dayarr[int(hh) + 4] == "false":
                    dayarr[int(hh)] = "false"
                if dayarr[int(hh) + 5] == "false":
                    dayarr[int(hh)] = "false"
            dayarr[36] = "false"
            dayarr[37] = "false"
            dayarr[38] = "false"
            dayarr[39] = "false"
            dayarr[40] = "false"
# ------------------------------------------------------------------------------------------


        timesel = [0]
        timesel.clear()

        for i in range(41):
            if dayarr[i] == "false":
                timesel.append(i-1)
        return timesel
    return []
def timebeforreserv(numberday,melicod):
    t = dt.now()
    t += timedelta(days=1 + int(numberday))
    reservs = reservemodel.objects.all()
    reservarray = []
    reservarray.clear()
    for reserv in reservs:
        if (int(reserv.personreserv) == int(melicod)) and (reserv.datemiladireserv == t.strftime('%a %d %b %y')):
            reservarray.append(int(reserv.numbertime)-1)
            # if int(reserv.timereserv)
            a = int(reserv.numbertime)-1
            for i in range(int(reserv.timereserv)):
                print('ppppppp',i)
                reservarray.append(a)
                a += 1

    return reservarray

def reservdef(request):
    print(11)
# ---------اگر فردی که وارد شده است login  کرده باشد اینجا برایش در reservmodeltest  یک object ساخته میشود-----------
    request.session['member'] = None
    member = request.POST.get('member')
    if (member != None) and (member != 'None' ) and (member != '' ):
        request.session['member'] = member
        request.session['recive-of'] = 'profile'
    else:
        request.session['member'] = request.user.username
        request.session['recive-of'] = 'my_reserv'
    melicode_reserv = request.session.get('member')
    rtotal = reservemodeltest.objects.all()
    for r in rtotal :
        if r.mellicode == melicode_reserv:
            melicodcheck = "true"

    # if melicodcheck == "false" :
    #     print()
    #     reservemodeltest.objects.create(
    #         mellicode= request.user.username,
    #         )
# ----------با توجه به کد ملی فرد login شده اسم کوچک و بزرگ او را پیدا میکنیم---------------------------
    users = accuntmodel.objects.all()
    for user in users:
        if user.melicode == melicode_reserv:
            level[0] = user.level
            mellicoduser[0] = user.melicode
            # a = reservemodeltest.objects.filter(mellicode=request.user.username)
            # a.update(fiestname=user.firstname, lastname=user.lastname , phonnumber=user.phonnumber)
    filesendbutton = request.POST.get("filesendbutton")
    inject_botax  = request.POST.get("r1")
    illnes  = request.POST.get("r2")
    drug = request.POST.get("drug")
    sensivety  = request.POST.get("r3")
    pregnancy  = request.POST.get("r4")
    date_finaly = request.POST.get("date_finaly")
    image_show = request.POST.get("c1")
    satisfact = request.POST.get("c4")
    inputwork = request.POST.get("inputwork")
    timeselect = request.POST.get("timeselect")
# ______________________________کلید صفحه reserv___________________________
    backbuttonfianal = request.POST.get("backbuttonfianal")
    if backbuttonfianal =="accept":
        # return redirect('http://127.0.0.1:8000/')
        return redirect("/")

# +++++++++++++++++++++++++++++کلید های صفحه reserv_end.html++همون که بزنی میره برا پرداخت+++++++++++++++++++++++++++
    peymentbutton = request.POST.get("peymentbutton")
    backbutton = request.POST.get("backbutton")
    if backbutton =="accept":
        # return redirect('http://127.0.0.1:8000/')
        return redirect("/")
    if peymentbutton == "accept":
        # return redirect('http://127.0.0.1:8000/zib/zibal/')
        return redirect('https://drmahdiasadpour.ir/zib/zibal/')
    # *******************************************************ساختن آرایه ها برای نمایش خدمتها در صفحه وب********************************************
    works = workmodel.objects.all()
    ww.clear()
    ww.append('start')
    for w in works :
        a = 0
        for x in ww :
            if x ==  w.work :
                a = 1
        if a == 0 :
            ww.append(w.work)
    ww.pop(0)
    # bers = esmekalamodel.objects.all()
#**********************انتخاب کاربر به صورت یک عدد از forloop  از وب میاد و در اینجا اون عدد تبدیل میشه به انتخاب اصلی و در  f  ریخته میشه**************
    workselectid = "None"
    try:
        workselectid = int(str(save_selection(request)).split('+')[0])
    except:
        workselectid = "None"

    c = 0
    personelmelicode = '0'
    berand = ''
    if workselectid != "None":
        reservposition[0] = "1"
        for f in works :
            if workselectid == f.id:
                selectprocedure.clear()
                selectprocedure.append(f.work)
                selectprocedure.append(f.detalework)
                selectprocedure.append(f.person)
                berand = f.berand
                personelmelicode = f.melicodpersonel
                # a = reservemodeltest.objects.filter(mellicode=request.user.username)
                # a.update(jobreserv=f.work,
                #          detalereserv=f.detalework,
                #          personreserv=f.person,
                #          vahed=f.vahed,
                #          idwork=f.id
                #          )
                sel = ''
                if f.time == "زمان کمی میبرد" :
                    sel = "0"
                    selectprocedure.append("0")
                if f.time == "پانزده دقیقه" :
                    sel = "1"
                    selectprocedure.append("1")
                if f.time == "سی دقیقه" :
                    sel = "2"
                    selectprocedure.append("2")
                if f.time =="چهل و پنج دقیقه" :
                    sel = "3"
                    selectprocedure.append("3")
                if f.time == "یک ساعت" :
                    sel = "4"
                    selectprocedure.append("4")
                if f.time == "یک ساعت و پانزده دقیقه" :
                    sel = "5"
                    selectprocedure.append("5")
                if f.time == "یک ساعت و نیم" :
                    sel = "6"
                    selectprocedure.append("6")
                selectprocedure.append(f.cast)
                # a = reservemodeltest.objects.filter(mellicode=request.user.username)
                # a.update(
                #          timereserv=sel,
                #          castreserv=f.cast,
                #          )

            c +=1

        shamsiarray.clear()
        miladiarray.clear()
        day.clear()
        reservmovaghats = reservemodeltest.objects.all()
        # ___________در این قسمت تعداد روزهایی که قرار هستش به مراجعه کننده نشون بدیم مشخص میشه____
        tedaderooz = 10
        # __________آرایه shmsiarray_ساخته میشه به تعداد tedaderooz  به ترتیب از امروز روز میچینه تو خودش________
        t = dt.now()
        t += timedelta(days=1)
        for i in range(tedaderooz) :
            shamsiarray.append(stradb(t))
            miladiarray.append(t.strftime('%a %d %b %y'))

# ____________در آرایه ی dayarr  بیست تا true مسازه که برای هر روز نشانه ازاد بودن بیست تایم ده صبح تا 8 شب هستش________
# _________بعد میاد محدودیتها رو اعمال میکنه و هذ تایم رو براساس محدودتها ممکنه false کنه یا true نگه داره_________
            dayarr = ['t']
            dayarr.clear()
            dayarr.append(stradb(t))
            for h in range(40):
                dayarr.append('true')
# _____برسی مرخصی ها و حضور اپراتوری که انتخاب شده_________
            ls = leavemodel.objects.all()
            for l in ls :
                if int(l.personelmelicod) == int(personelmelicode):
                    if l.muont == strb(t) :
                        s = l.leave.split(",")
                        a = 2
                        for iii in range(int(len(s))):
                            if a <= len(s):
                                if s[a] == strd(t):
                                    dayarr[int(s[a-1])] = "false"
                                a += 2
                            else:
                                break
# ---------وقتی یه نفر یه کاری رو انتخاب میکنه تا قبل از پرداخت براش رزرو میشه تا کس دیگه ای تو این فاصله نتونه رزروش کنه--------
            for reservmovaghat in reservmovaghats:
                if reservmovaghat.personreserv == selectprocedure[2]:
                    if reservmovaghat.dateshamsireserv == stradb(t):
                        if reservmovaghat.timereserv == '1':
                            dayarr[int(reservmovaghat.numbertime)] = "false"
                        if reservmovaghat.timereserv == '2':
                            dayarr[int(reservmovaghat.numbertime)] = "false"
                            dayarr[int(reservmovaghat.numbertime) + 1] = "false"
                        if reservmovaghat.timereserv == '3':
                            dayarr[int(reservmovaghat.numbertime)] = "false"
                            dayarr[int(reservmovaghat.numbertime) + 1] = "false"
                            dayarr[int(reservmovaghat.numbertime) + 2] = "false"
                        if reservmovaghat.timereserv == '4':
                            dayarr[int(reservmovaghat.numbertime)] = "false"
                            dayarr[int(reservmovaghat.numbertime) + 1] = "false"
                            dayarr[int(reservmovaghat.numbertime) + 2] = "false"
                            dayarr[int(reservmovaghat.numbertime) + 3] = "false"
                        if reservmovaghat.timereserv == '5':
                            dayarr[int(reservmovaghat.numbertime)] = "false"
                            dayarr[int(reservmovaghat.numbertime) + 1] = "false"
                            dayarr[int(reservmovaghat.numbertime) + 2] = "false"
                            dayarr[int(reservmovaghat.numbertime) + 3] = "false"
                            dayarr[int(reservmovaghat.numbertime) + 4] = "false"
                        if reservmovaghat.timereserv == '6':
                            dayarr[int(reservmovaghat.numbertime)] = "false"
                            dayarr[int(reservmovaghat.numbertime) + 1] = "false"
                            dayarr[int(reservmovaghat.numbertime) + 2] = "false"
                            dayarr[int(reservmovaghat.numbertime) + 3] = "false"
                            dayarr[int(reservmovaghat.numbertime) + 4] = "false"
                            dayarr[int(reservmovaghat.numbertime) + 5] = "false"

    # -------------------------اینجا رزرو های قبلی رو چک میکنه---------
            res = reservemodel.objects.all()
            for r in res :
                if r.personreserv == selectprocedure[2] :
                    if r.dateshamsireserv == stradb(t) :
                        if r.timereserv == '1' :
                            dayarr[int(r.numbertime)] = "false"
                        if r.timereserv == '2' :
                            dayarr[int(r.numbertime)] = "false"
                            dayarr[int(r.numbertime) + 1] = "false"
                        if r.timereserv == '3' :
                            dayarr[int(r.numbertime)] = "false"
                            dayarr[int(r.numbertime) + 1] = "false"
                            dayarr[int(r.numbertime) + 2] = "false"
                        if r.timereserv == '4' :
                            dayarr[int(r.numbertime)] = "false"
                            dayarr[int(r.numbertime) + 1] = "false"
                            dayarr[int(r.numbertime) + 2] = "false"
                            dayarr[int(r.numbertime) + 3] = "false"
                        if r.timereserv == '5' :
                            dayarr[int(r.numbertime)] = "false"
                            dayarr[int(r.numbertime) + 1] = "false"
                            dayarr[int(r.numbertime) + 2] = "false"
                            dayarr[int(r.numbertime) + 3] = "false"
                            dayarr[int(r.numbertime) + 4] = "false"
                        if r.timereserv == '6':
                            dayarr[int(r.numbertime)] = "false"
                            dayarr[int(r.numbertime) + 1] = "false"
                            dayarr[int(r.numbertime) + 2] = "false"
                            dayarr[int(r.numbertime) + 3] = "false"
                            dayarr[int(r.numbertime) + 4] = "false"
                            dayarr[int(r.numbertime) + 5] = "false"
            # # ---------------------------------------------اگر کاری مه انتخاب شده بیش از نیم ساعت باشه یعنی دو تا نیم ساغت یا سه  یا پهارتا یا پنج تا نیم ساعت باشه-----------
# # ------باید چک شود که تا تایم های اینده اش  به همون اندازه که وقت میخواد وقت باشه ---------------------------------------
#
            if selectprocedure[3] == "2" :
                for hh in range(19) :
                    hh += 1
                    if dayarr[int(hh) + 1] == "false" :
                        dayarr[int(hh)] = "false"
                dayarr[40] = "false"
            if selectprocedure[3] == "3" :
                for hh in range(18) :
                    hh += 1
                    if dayarr[int(hh) + 1] == "false" :
                        dayarr[int(hh)] = "false"
                    if dayarr[int(hh) + 2] == "false":
                        dayarr[int(hh)] = "false"
                dayarr[39] = "false"
                dayarr[40] = "false"
            if selectprocedure[3] == "4" :
                for hh in range(17) :
                    hh += 1
                    if dayarr[int(hh) + 1] == "false" :
                        dayarr[int(hh)] = "false"
                    if dayarr[int(hh) + 2] == "false":
                        dayarr[int(hh)] = "false"
                    if dayarr[int(hh) + 3] == "false":
                        dayarr[int(hh)] = "false"
                dayarr[38] = "false"
                dayarr[39] = "false"
                dayarr[40] = "false"
            if selectprocedure[3] == "5" :
                for hh in range(16) :
                    hh += 1
                    if dayarr[int(hh) + 1] == "false" :
                        dayarr[int(hh)] = "false"
                    if dayarr[int(hh) + 2] == "false" :
                        dayarr[int(hh)] = "false"
                    if dayarr[int(hh) + 3] == "false" :
                        dayarr[int(hh)] = "false"
                    if dayarr[int(hh) + 4] == "false" :
                        dayarr[int(hh)] = "false"
                dayarr[37] = "false"
                dayarr[38] = "false"
                dayarr[39] = "false"
                dayarr[40] = "false"
            if selectprocedure[3] == "6" :
                for hh in range(15) :
                    hh += 1
                    if dayarr[int(hh) + 1] == "false" :
                        dayarr[int(hh)] = "false"
                    if dayarr[int(hh) + 2] == "false" :
                        dayarr[int(hh)] = "false"
                    if dayarr[int(hh) + 3] == "false" :
                        dayarr[int(hh)] = "false"
                    if dayarr[int(hh) + 4] == "false" :
                        dayarr[int(hh)] = "false"
                    if dayarr[int(hh) + 5] == "false":
                        dayarr[int(hh)] = "false"
                dayarr[36] = "false"
                dayarr[37] = "false"
                dayarr[38] = "false"
                dayarr[39] = "false"
                dayarr[40] = "false"

#
            t += timedelta(days=1)
            day.append(dayarr)
# --------------------------اگر ابن دوخظ انجام شه دو دیتای اول در ارایه ی روزها پاک خواهد شد یعنی ار دو روز بعد میتونن نوبا بگیرن--------------
# -----ولی اگه بخوایم این کار رو بکنیم باید ارایه های شمسی و میلادی هم از دوتا دور تر خونده بشن یغنی یغنی خط.ط 301 و 302 عوض شنبه جای اینکه از اول خوانده بشن از دوتا جلوتر خوانده بشن
        # day.pop(0)
        # day.pop(0)
        return render(request,'new_timereserv.html',context={
                                                         'day':day,
                                                         'person':" رزرو وقت برای " + selectprocedure[0] +" "+ selectprocedure[1] + ' '+ berand +' '+ "(" + selectprocedure[2] + ")",
                                                         })
# _______انتخاب یه تایم برای خدمت مورد نظر__________
    if (timeselect != None) and (timeselect != '') :
        # reservposition[0] = 2
        s = timeselect
        stime = s.split(",")
        ttime = dt.now()
        ttime += timedelta(days=1)
        for tt in range(int(stime[1])) :
            ttime += timedelta(days=1)
        ttime -= timedelta(days=1)
        # a = reservemodeltest.objects.filter(mellicode=request.user.username)
        # a.update(
        #     dateshamsireserv=stradb(ttime),
        #     datemiladireserv=ttime.strftime('%a %d %b %y'),
        #     yearshamsi=stry(datetime.datetime.now()),
        #     numbertime=stime[0],
        # )
        selectprocedure.append(stradb(ttime))
        selectprocedure.append(ttime.strftime('%a %d %b %y'))
        selectprocedure.append(stry(dt.now()))
        selectprocedure.append(stime[0])
        s = ""
        if stime[0] == "1"  :
            s ="10"
            selectprocedure.append("10:00")
        if stime[0] == "2"  :
            s ="10:15"
            selectprocedure.append("10:15")
        if stime[0] == "3"  :
            s ="10:30"
            selectprocedure.append("10:30")
        if stime[0] == "4"  :
            s ="10:45"
            selectprocedure.append("10:45")
        if stime[0] == "5"  :
            s ="11"
            selectprocedure.append("11:00")
        if stime[0] == "6"  :
            s ="11:15"
            selectprocedure.append("11:15")
        if stime[0] == "7"  :
            s ="11:30"
            selectprocedure.append("11:30")
        if stime[0] == "8"  :
            s ="11:45"
            selectprocedure.append("11:45")
        if stime[0] == "9"  :
            s ="12"
            selectprocedure.append("12:00")
        if stime[0] == "10"  :
            s ="12:15"
            selectprocedure.append("12:15")
        if stime[0] == "11"  :
            s ="12:30"
            selectprocedure.append("12:30")
        if stime[0] == "12"  :
            s ="12:45"
            selectprocedure.append("12:45")
        if stime[0] == "13"  :
            s ="13"
            selectprocedure.append("13:00")
        if stime[0] == "14"  :
            s ="13:15"
            selectprocedure.append("13:15")
        if stime[0] == "15"  :
            s ="13:30"
            selectprocedure.append("13:30")
        if stime[0] == "16"  :
            s ="13:45"
            selectprocedure.append("13:45")
        if stime[0] == "17"  :
            s ="14"
            selectprocedure.append("14:00")
        if stime[0] == "18"  :
            s ="14:15"
            selectprocedure.append("14:15")
        if stime[0] == "19"  :
            s ="14:30"
            selectprocedure.append("14:30")
        if stime[0] == "20"  :
            s ="14:45"
            selectprocedure.append("14:45")
        if stime[0] == "21"  :
            s ="15"
            selectprocedure.append("15:00")
        if stime[0] == "22"  :
            s ="15:15"
            selectprocedure.append("15:15")
        if stime[0] == "23"  :
            s ="15:30"
            selectprocedure.append("15:30")
        if stime[0] == "24"  :
            s ="15:45"
            selectprocedure.append("15:45")
        if stime[0] == "25"  :
            s ="16"
            selectprocedure.append("16:00")
        if stime[0] == "26"  :
            s ="16:15"
            selectprocedure.append("16:15")
        if stime[0] == "27"  :
            s ="16:30"
            selectprocedure.append("16:30")
        if stime[0] == "28"  :
            s ="16:45"
            selectprocedure.append("16:45")
        if stime[0] == "29"  :
            s ="17"
            selectprocedure.append("17:00")
        if stime[0] == "30"  :
            s ="17:15"
            selectprocedure.append("17:15")
        if stime[0] == "31"  :
            s ="17:30"
            selectprocedure.append("17:30")
        if stime[0] == "32"  :
            s ="17:45"
            selectprocedure.append("17:45")
        if stime[0] == "33"  :
            s ="18"
            selectprocedure.append("18:00")
        if stime[0] == "34"  :
            s ="18:15"
            selectprocedure.append("18:15")
        if stime[0] == "35"  :
            s ="18:30"
            selectprocedure.append("18:30")
        if stime[0] == "36"  :
            s ="18:45"
            selectprocedure.append("18:45")
        if stime[0] == "37"  :
            s ="19"
            selectprocedure.append("19:00")
        if stime[0] == "38"  :
            s ="19:15"
            selectprocedure.append("19:15")
        if stime[0] == "39"  :
            s ="19:30"
            selectprocedure.append("19:30")
        if stime[0] == "40"  :
            s ="19:45"
            selectprocedure.append("19:45")
        # a = reservemodeltest.objects.filter(mellicode=request.user.username)
        # a.update(hourreserv=s)
        reservs = reservemodel.objects.all()
        reservetebar[0] = 'succes'
        filepage1 = "false"
        page =filepage1model.objects.all()
        for p in page :
            if p.mellicode == melicode_reserv :
                filepage1 = "true"
        if filepage1 == "false" :
            return render(request,'add_userfilebotax.html')
        else:
            rtotal = reservemodeltest.objects.all()
            for r in rtotal:
                if r.mellicode == melicode_reserv:
                    work = r.jobreserv
                    detalework = r.detalereserv
                    personwork = r.personreserv
                    dateshamsi = r.dateshamsireserv
                    hoursreserv = r.hourreserv
                    firstname = r.fiestname
                    lastname = r.lastname

            return render(request, 'reserv_end.html', context={
                                                                            "work" : work,
                                                                            "detalework" : detalework,
                                                                            "personwork" :personwork,
                                                                            "dateshamsi" : dateshamsi,
                                                                            "hoursreserv" :hoursreserv,
                                                                            "firstname" : firstname,
                                                                            "firstname" : firstname,
                                                                            "lastname" : lastname,
                                                                            })

# ___________________تشکیل پرونده___________
    if filesendbutton == "accept" :
        reservposition[0] = "3"
        if (inject_botax == "yes") or (inject_botax == "no") :
            file_botax[0] = inject_botax
        else:
            error = "inject_botax"
            return render(request, 'add_userfilebotax.html', context={"error": error,
                                                                                   'f':timeselect,
                                                                                  })
        if (illnes == "yes") or (illnes == "no"):
            file_botax[1] = illnes
        else:
            error = "illnes"
            return render(request, 'add_userfilebotax.html', context={"error": error})
        file_botax[2] = drug
        if (sensivety == "yes") or (sensivety == "no"):
            file_botax[3] = sensivety
        else:
            error = "sensivety"
            return render(request, 'add_userfilebotax.html', context={"error": error})
        if (pregnancy == "yes") or (pregnancy == "no"):
            file_botax[4] = pregnancy
        else:
            error = "pregnancy"
            return render(request, 'add_userfilebotax.html', context={"error": error})
        file_botax[5] = date_finaly
        if (image_show == "با انتشار تصویرم به صورت واضح در فضای مجازی مشکل ندارم") or (image_show == "با انتشار تصویرم به صورت غیرواضح در فضای مجازی مشکل ندارم") or (image_show == "با انتشار تصویرم در فضای مجازی مشکل دارم"):
            file_botax[6] = image_show
        else:
            error = "imgshow"
            return render(request, 'add_userfilebotax.html', context={"error": error})
        if satisfact == "yes":
            file_botax[9] = satisfact
        else:
            error = "satisfact"
            return render(request, 'add_userfilebotax.html', context={"error": error})
        filepage1model.objects.create(
            mellicode=mellicoduser[0],
            inject_botax=inject_botax,
            illnes=illnes,
            drug = drug,
            sensivety = sensivety,
            pregnancy = pregnancy,
            date_finaly = date_finaly,
            image_show = image_show,
            satisfact = satisfact,
                                       )

        b = ''
        rtotal = reservemodeltest.objects.all()
        for r in rtotal:
            if r.mellicode == melicode_reserv:
                wo = workmodel.objects.all()
                for woo in wo:
                    if int(r.idwork) == woo.id:
                        b = woo.berand
                work = r.jobreserv
                detalework = r.detalereserv
                personwork = r.personreserv
                dateshamsi = r.dateshamsireserv
                hoursreserv = r.hourreserv
                firstname = r.fiestname
                lastname = r.lastname


        return render(request, 'reserv_end.html', context={
                                                                        "work": work,
                                                                        "detalework": detalework,
                                                                        "personwork": personwork,
                                                                        "dateshamsi": dateshamsi,
                                                                        "hoursreserv": hoursreserv,
                                                                        "firstname": firstname,
                                                                        "firstname": firstname,
                                                                        "lastname": lastname,
                                                                        "berand":b,
                                                                    })


    nationalcode = melicode_reserv

    profilestatus = ''
    img = ''
    us = accuntmodel.objects.all()
    for u in us:
        if u.melicode == melicode_reserv:
            profilestatus = f"{u.firstname} {u.lastname}  "
            if u.profile_picture and hasattr(u.profile_picture, 'url'):
                img = u.profile_picture.url
            else:
                img = '/static/img/login.jpg'
            break;

    return render(request,'new_reserv.html',context={
        'img':img,
        'profilestatus':profilestatus,
        'works':works,
        'job':ww,
        'nationalcode':nationalcode,
         })
    # else:
    #     loginetebar[0] = "false"
    #     return render(request,'home.html',context={"loginetebar":loginetebar[0]})

# _________________________اینجا کارمندان تایمهایی که قرار هست نیان سر کار رو مشخص میکن و در leavemodel.leave_ ذخیره میکنن_____________
leaveshamsi = ['0']
leavemiladi = ['0']
leavearray = ['0']

def reserverdef(request):
    etebarreservdasti = 'false'
    dayselect = request.POST.get('day')
    mounthselect = request.POST.get('mounth')
    if dayselect == None :
        dayselect = '0'
    if mounthselect == None :
        mounthselect = '0'

    idreserv = request.POST.get("idreserv")
    buttondelet = request.POST.get("buttondelet")
    buttoncancel =request.POST.get("buttoncancel")
    operatoreselect = request.POST.get("operatoreselect")
    operatormelicod = request.POST.get("operatormelicod")
    if (operatormelicod == None) or (operatormelicod == '') or (operatormelicod == 'None'):
        operatormelicod = operatoreselect
    timeselect = request.POST.get('timeselect')
    timesel = request.POST.get('timesel')
    namebuttom =request.POST.get('namebuttom')
    names = request.POST.get('names')
    tickon = request.POST.get('tickon')
    melicode = request.POST.get('melicode')
    etebarmelicod = request.POST.get('etebarmelicod')
    job = request.POST.get('job')
    jobbuttom = request.POST.get('jobbuttom')
    button_send =request.POST.get("button_send")
    detalework = request.POST.get("detalework")
    pey = request.POST.get("pey")
    bankpey = request.POST.get("bankpey")
    if (pey == '') or (pey == None):
        pey = '0'
        bankpey = '-2'
    yu = int(bankpey)
    #
    # if (bankpey == '') or (bankpey == None):
    #     bankpey = '-2'
    # ------تولید لیست حسابهای بانکی در hesabs-و کار انتخاب شده رو میریزه توی b----
    banks = bankmodel.objects.all()
    hesabs = [""]
    hesabs.clear()
    for bank in banks:
        r = 0
        for hesab in hesabs:
            if hesab[1] == bank.onvan:
                r = 1
        if r == 0:
            s = (str(bank.id) + "," + str(bank.onvan)).split(",")
            hesabs.append(s)

    # --------------------------------------------------------------------------------

    # dayconter = request.POST.get("dayconter")
    # if (dayconter == None) or (dayconter == 'None') or (dayconter == ''):
    #     dayconter = 0

    if buttondelet == 'accept' :
        a = reservemodel.objects.filter(id=int(idreserv))
        a.delete()
# ----------------یه آرایه میسازه و همه کارمندان رو نیریزه توش تا اتنخاب کنند همچنین کنترل میکنه که اون
    # کارمند انتخاب شده با زدن دکمه های روز بعد و روز قبل یا هر دکمه دیگه حفظ بشه ---
    operatorarray = ['']
    operatorarray.clear()
    tekrarcheck = ['']
    tekrarcheck.clear()
    ws = workmodel.objects.all()
    for w in ws:
        c = "true"
        for n in operatorarray:
            if n[1] == w.melicodpersonel :
                c = 'false'
        if c == "true" :
            p = (w.person + "," + str(w.melicodpersonel)).split(",")
            operatorarray.append(p)
    personel = ''
    melicodperonel = '1'
    if (operatoreselect != "None") and (operatoreselect != None) and (operatoreselect != ''):
        users = accuntmodel.objects.all()
        for user in users:
            if int(user.melicode) == int(operatoreselect) :
                personel = user.firstname + " " + user.lastname
                melicodperonel = user.melicode


# - اینچا یه رایه میسازه و همون بیست تایم رو توش میذاره و بعد ار reservmodel رزرو ها و خارج از نوبت ها رو میاره بعد
    # کلید روز بغد و روز قبل رو هدلیت میکنه و اینکه چند روز از امروز جلوتر رفتیم یا عقب تر رفتیم رو در dayconter میریزه---

    t = dt.now()
    a = 0
    dayconterstr = request.POST.get("dayconter")
    if (dayconterstr == None) or (dayconterstr == "") or (dayconterstr == 'None'):
        dayconter = 0
    else:
        dayconter = int(dayconterstr)

    button_next = request.POST.get("button_next")
    if button_next == 'accept' :
        a = 1
        dayconter += 1
    button_back = request.POST.get("button_back")
    if button_back == 'accept' :
        a = 1
        dayconter -= 1

    if dayconter < 0 :
        dayconterm = dayconter * (-1)
        for i in range(dayconterm):
            t -= timedelta(days=1)

    if dayconter > 0 :
        for i in range(dayconter):
            t += timedelta(days=1)
    y = stry(t)
    e = ''
    if a == 0 :
        if (dayselect != '0') and (mounthselect != '0') :
            if (int(strd(t)) >= int(dayselect)) and (strb(t) == mounthselect):
                while strb(t) == mounthselect:
                    t -= timedelta(days=1)
                    dayconter -= 1

            while strb(t) != mounthselect:
                t += timedelta(days=1)
                dayconter += 1
                if int(y) != int(stry(t)):
                    e = 'false'
                    break
            while int(strd(t)) != int(dayselect):
                t += timedelta(days=1)
                dayconter += 1



    dayreserv = ['t']
    dayreserv.clear()
    dayarr = ['t']
    dayarr.clear()
    dayarr.append(stradb(t))
    for h in range(41):
        dayarr.append('')
    rs = reservemodel.objects.all()
    name = ''
    ls = leavemodel.objects.all()
    for l in ls:
        if int(l.personelmelicod) == int(melicodperonel):
            if l.muont == strb(t):
                s = l.leave.split(",")
                a = 2
                for iii in range(int(len(s))):
                    if a <= len(s):
                        if s[a] == strd(t):
                            dayarr[int(s[a - 1])] = "false"
                        a += 2
                    else:
                        break

    for r in rs:
        if (r.datemiladireserv == t.strftime('%a %d %b %y')) and (r.personreserv == personel ) and (r.vaziyatereserv != 'کنسل'):
            us = accuntmodel.objects.all()
            for u in us:
                if r.melicod == u.melicode :
                    name = u.firstname + " " + u.lastname
            dayarr[int(r.numbertime)] =r.vaziyatereserv+'    ' +name + " " + r.jobreserv + " " + r.detalereserv + " " + r.personreserv + " " + "بیعانه:" + " " + r.pyment
            i = 1
            while i < int(r.timereserv):
                dayarr[int(r.numbertime)+i] = "false"
                i += 1

    ps = fpeseshktestmodel.objects.all()
    name = ''
    for p in ps:
        if (p.datemiladireserv == t.strftime('%a %d %b %y')) and (p.personreserv == personel ) :
            us = accuntmodel.objects.all()
            for u in us:
                if p.melicod == u.melicode :
                    name = u.firstname + " " + u.lastname
            dayarr[int(p.numbertime)] ='قطعی'+'    '+name + " " + p.jobreserv + " " + p.detalereserv + " " + p.personreserv
            # dayarr[int(p.numbertime)] = "false"
            i = 1
            while i < int(p.timereserv):
                dayarr[int(p.numbertime)+i] = "false"
                i += 1


    dayreserv.append(dayarr)

    dastiarray = ['']
    dastiarray.clear()
    rs = reservemodel.objects.all()
    for r in rs:
        if (r.datemiladireserv == t.strftime('%a %d %b %y')) and (r.personreserv == personel ) and (r.numbertime == "41"):
            us = accuntmodel.objects.all()
            for u in us:
                if r.melicod == u.melicode :
                    name = u.firstname + " " + u.lastname
            dastiarray.append([(name + " " + r.jobreserv + " " + r.detalereserv + " " + r.personreserv ),str(r.id)])

# ----------------------------------------------------------------------------------------------------------------------------------
    personreserv = ''
    if button_send == 'accept':
        intdayconter = int(dayconter)
        tm = dt.now()
        while intdayconter > 0:
            tm += timedelta(days=1)
            intdayconter -= 1
        while intdayconter < 0:
            tm -= timedelta(days=1)
            intdayconter += 1
        etebarreservdasti = 'true'
        users = accuntmodel.objects.all()
        for user in users:
            if int(user.melicode) == int(operatormelicod):
                personreserv = user.firstname + ' ' + user.lastname
        ws = workmodel.objects.all()
        jobreserv = ''
        detalereserv = ''
        castreserv = ''
        vahed = ''
        numbertime = ''
        for w in ws:
            if int(w.id) == int(detalework):
                jobreserv = w.work
                detalereserv = w.detalework
                castreserv = w.cast
                vahed =w.vahed
                numbertime = w.time
        stime = ['']
        stime[0] = timesel
        s =''
        if 1==1 :
            if stime[0] == "1":
                s = "10:00"
            if stime[0] == "2":
                s = "10:15"
            if stime[0] == "3":
                s = "10:30"
            if stime[0] == "4":
                s = "10:45"
            if stime[0] == "5":
                s = "11:00"
            if stime[0] == "6":
                s = "11:15"
            if stime[0] == "7":
                s = "11:30"
            if stime[0] == "8":
                s = "11:45"
            if stime[0] == "9":
                s = "12:00"
            if stime[0] == "10":
                s = "12:15"
            if stime[0] == "11":
                s = "12:30"
            if stime[0] == "12":
                s = "12:45"
            if stime[0] == "13":
                s = "13:00"
            if stime[0] == "14":
                s = "13:15"
            if stime[0] == "15":
                s = "13:30"
            if stime[0] == "16":
                s = "13:45"
            if stime[0] == "17":
                s = "14:00"
            if stime[0] == "18":
                s = "14:15"
            if stime[0] == "19":
                s = "14:30"
            if stime[0] == "20":
                s = "14:45"
            if stime[0] == "21":
                s = "15:00"
            if stime[0] == "22":
                s = "15:15"
            if stime[0] == "23":
                s = "15:30"
            if stime[0] == "24":
                s = "15:45"
            if stime[0] == "25":
                s = "16:00"
            if stime[0] == "26":
                s = "16:15"
            if stime[0] == "27":
                s = "16:30"
            if stime[0] == "28":
                s = "16:45"
            if stime[0] == "29":
                s = "17:00"
            if stime[0] == "30":
                s = "17:15"
            if stime[0] == "31":
                s = "17:30"
            if stime[0] == "32":
                s = "17:45"
            if stime[0] == "33":
                s = "18:00"
            if stime[0] == "34":
                s = "18:15"
            if stime[0] == "35":
                s = "18:30"
            if stime[0] == "36":
                s = "18:45"
            if stime[0] == "37":
                s = "19:00"
            if stime[0] == "38":
                s = "19:15"
            if stime[0] == "39":
                s = "19:30"
            if stime[0] == "40":
                s = "19:45"
            if stime[0] == "41":
                s = "20"
        sel = ''
        if 1==1:
            sel = ''
            if numbertime == "زمان کمی میبرد":
                sel = "0"
                selectprocedure.append("0")
            if numbertime == "پانزده دقیقه":
                sel = "1"
                selectprocedure.append("1")
            if numbertime == "سی دقیقه":
                sel = "2"
                selectprocedure.append("2")
            if numbertime == "چهل و پنج دقیقه":
                sel = "3"
                selectprocedure.append("3")
            if numbertime == "یک ساعت":
                sel = "4"
                selectprocedure.append("4")
            if numbertime == "یک ساعت و پانزده دقیقه":
                sel = "5"
                selectprocedure.append("5")
            if numbertime == "یک ساعت و نیم":
                sel = "6"
                selectprocedure.append("6")

        reservemodel.objects.create(
            melicod=melicode,
            jobreserv = jobreserv,
            detalereserv = detalereserv,
            personreserv =personreserv,
            timereserv = sel,
            castreserv = castreserv,
            numbertime = timesel,
            hourreserv = s,
            dateshamsireserv = stradb(tm),
            datemiladireserv = tm.strftime('%a %d %b %y'),
            yearshamsi = stry(dt.now()),
            vahed = vahed,
            idwork=detalework,
            pyment=pey,
            bankpeyment=bankpey,

        )
        nam = ''
        users = accuntmodel.objects.all()
        for user in users:
            if int(user.melicode) == int(melicode) :
                nam = user.firstname + ' ' + user.lastname
                r = random.randint(1000, 9999)
                smstext = nam + ' ' + 'عزیز' + '\n' + 'خدمت' +' ' + jobreserv + ' ' + detalereserv +' '+'در روز'+' ' +stradb(tm)+ ' ' + 'ساعت'+' '+s+' '+' برای شما رزرو گردید'+'\n' + 'با تشکر' + 'مطب دکتر اسدپور' + '\n'+ 'کد ثبت دفتر:'+' '+str(r)+'\n' + '\n' + '\n' + 'لغو ارسال پیامک 11'
                try:
                    api = KavenegarAPI(
                        '527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D')
                    params = {
                        'sender': '9982003178',  # optional
                        'receptor': user.phonnumber,  # multiple mobile number, split by comma
                        'message': smstext,
                    }
                    response = api.sms_send(params)
                except APIException as e:
                    m = 'tellerror'
                except HTTPException as e:
                    m = 'neterror'

        tcheck = dt.now()
        etebartime = 'false'
        for i in range(400):
            tcheck += timedelta(days=1)
            if tm.strftime('%a %d %b %y') == tcheck.strftime('%a %d %b %y'):
                etebartime = 'true'
                break
            
        # users = accuntmodel.objects.all()
        # for user in users:
        #     if (int(user.melicode) == int(melicode)) and (etebartime == 'true') :
        #         try:
        #             api = KavenegarAPI(
        #                 '527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D')
        #             params = {
        #                 'sender': '9982003178',  # optional
        #                 'receptor': user.phonnumber,  # multiple mobile number, split by comma
        #                 'message':" سلام",
        #             }
        #             response = api.sms_send(params)
        #             # return render(request, 'code_cantact.html')
        #         except APIException as e:
        #             m = 'tellerror'
        #             return render(request, 'closecash.html', context={'melicod_etebar': m})
        #         except HTTPException as e:
        #             m = 'neterror'
        #             return render(request, 'closecash.html', context={'melicod_etebar': m}, )

        return render(request, 'reserver.html', context={
            'dastiarray': dastiarray,
            'day': dayreserv,
            'operatorarray': operatorarray,
            'operatoreselect': operatoreselect,
            'dayconter': dayconter,
            'personel': personel,
            'melicodperonel': melicodperonel,
            'dayselect': dayselect,
            'mounthselect': mounthselect,
            'e': e,
            'bank': hesabs,
        })

    # ------از جدول وقتها یکی انتخاب میشه سه حالت داره یا یه تایم قبلی هستش یا یه تایم حارج از وقت یا تایم خالی  ------
    if ( timeselect != None ) and ( timeselect != '' ):
        se = timeselect.split(",")
        tt = int(se[1])

        timesel = int(se[0])

        intdayconter = int(dayconter)
        time = dt.now()
        while intdayconter > 0:
            time += timedelta(days=1)
            intdayconter -= 1
        while intdayconter < 0:
            time -= timedelta(days=1)
            intdayconter += 1

        reservs = reservemodel.objects.all()
        for reserv in reservs:
            if str(int(se[0])) == "41":
                if str(reserv.id) == str(int(se[1])):
                    n = ''
                    qs = accuntmodel.objects.all()
                    for q in qs:
                        if q.melicode == reserv.melicod:
                            n = q.firstname + " " + q.lastname +'\n'+q.phonnumber

                    return render(request,'remove_reserv.html.',context={
                        'moraje':n,
                        'operat':reserv.personreserv,
                        'timereserv':reserv.dateshamsireserv+ ' ' +reserv.hourreserv + ' ' + reserv.jobreserv + ' ' + reserv.detalereserv,
                        'idreserv':reserv.id,
                        'bank': hesabs,
                    })
            else:
                if (reserv.personreserv == personel) and (reserv.datemiladireserv == time.strftime('%a %d %b %y')) and ( int(se[0]) == int(reserv.numbertime)) :
                    n = ''
                    qs = accuntmodel.objects.all()
                    for q in qs:
                        if q.melicode == reserv.melicod:
                            n = q.firstname + " " + q.lastname+'\n'+q.phonnumber

                    return render(request,'remove_reserv.html',context={
                        'moraje':n,
                        'operat':reserv.personreserv,
                        'timereserv':reserv.dateshamsireserv+ ' ' +reserv.hourreserv + ' ' + reserv.jobreserv + ' ' + reserv.detalereserv,
                        'idreserv':reserv.id,
                        'bank': hesabs,
                    })
        return render(request,'reserv_reserver.html',context={
            'operatormelicod':operatormelicod,
            'dayconter':dayconter,
            'timesel':timesel,
            'bank': hesabs,
        })
# -------------------------------------------------------------------------------------------------------------------------------------
# ------------میاد سه حرف اول اسم یا فامیل رو میگیره و بعد لبست اسامی
    # رو تهیه میکنه و میریزه تو ارایه arraynameهمراه با این ارایه مد ملی اپراتور که از اول تو جدول تایمش بودیم رو میقرسته-------
    arrayname =['']
    if namebuttom == 'accept':
        ls = searchmodeltest.objects.all()
        for l in ls:
            a = searchmodeltest.objects.filter(m=l.m)
            a.delete()
        arrayname.clear()

        auser = accuntmodel.objects.all()
        amaray = ['']
        amaray.clear()
        for uss in auser:
            if uss.firstname[0:3] == names :
                mm = ['']
                mm.clear()
                mm.append(uss.firstname + " " + uss.lastname)
                mm.append(uss.melicode)
                amaray.append(uss.melicode)
                mm.append(uss.phonnumber)
                searchmodeltest.objects.create(m=uss.melicode)
                arrayname.append(mm)
        for aa in auser:
            if aa.lastname[0:3] == names :
                cheek = "true"
                for archek in amaray:
                    if archek == aa.melicode :
                        cheek = "false"
                if cheek == "true" :
                    mm = ['']
                    mm.clear()
                    mm.append(aa.firstname + " " + aa.lastname)
                    mm.append(aa.melicode)
                    mm.append(aa.phonnumber)
                    searchmodeltest.objects.create(m=aa.melicode)
                    arrayname.append(mm)
        return render(request,'reserv_reserver.html',context={
            'operatormelicod': operatormelicod,
            'dayconter': dayconter,
            'arrayname':arrayname,
            'timesel':timesel,
            'bank': hesabs,
        })
# -------------------------------------------------------------------------------------------------------------------------------
# -----در اینچا کد ملی اپراتور که از اول در تایمش بودیم رو میاره به عنوان اپراتور در صفحه ای که میخوای خدمت رو انتخاب کنی -----
    ls = searchmodeltest.objects.all()
    if (tickon != None) and (tickon != ''):
        inttikon = int(tickon)
        ar = ['']
        ar.clear()
        for l in ls :
            ar.append(l.m)
                           # -- چون سرور بر عکس ترتیه ها رو میخونه ایمچا و در cash viwo . cast این کامنت هست-
        ar.reverse()
        melicode = ar[inttikon]
        users = accuntmodel.objects.all()
        if (melicode != None) and (melicode != ''):
            etebarmelicod = "false"
            for user in users:
                if user.melicode == melicode:
                    name = user.firstname + " " + user.lastname
                    etebarmelicod = "true"
        personel = ''
        for user in users:
            if int(user.melicode) == int(operatormelicod):
                personel = user.firstname + ' ' + user.lastname

        jobarray = ['']
        jobarray.clear()
        ws = workmodel.objects.all()
        for w in ws:
            if int(w.melicodpersonel) == int(operatormelicod):
                et = "true"
                for ja in jobarray:
                    if ja[0] == w.work:
                        et = "false"
                if et == "true":
                    s = (w.work + "," + str(w.idjob)).split(",")
                    jobarray.append(s)
                    etebarmelicod = "true"
        return render(request,'reserv_reserver.html',context={
            'operatormelicod': operatormelicod,
            'melicode':melicode,
            'name':name,
            'etebarmelicod':etebarmelicod,
            'personel':personel,
            'jobs': jobarray,
            'dayconter': dayconter,
            'timesel':timesel,
            'bank': hesabs,
        })

# -------------------------------------------------------------------------------------------------------------------------------------
# ----وقتی که کنار یک اسم تیک زدهه میشه وارد
    # صفحه رزرو میبشه اینجا قبل از اینکه وارد این صفحه بشه فایل jobarray  رو میسازه و میفرسته تا انتخاب کنه------
    if (melicode != None) and (melicode != 'None') and (melicode != '') and (jobbuttom != 'accept') :
        jobarray = ['']
        jobarray.clear()
        ws = workmodel.objects.all()
        for w in ws:
            if int(w.melicodpersonel) == int(operatormelicod):
                et = "true"
                for ja in jobarray:
                    if ja[0] == w.work:
                        et = "false"
                if et == "true":
                    s = (w.work + "," + str(w.idjob)).split(",")
                    jobarray.append(s)
        return render(request, 'reserv_reserver.html', context={
            'operatormelicod': operatormelicod,
            'melicode': melicode,
            'name': name,
            'etebarmelicod': etebarmelicod,
            'personel': personel,
            'jobs':jobarray,
            'dayconter': dayconter,
            'timesel':timesel,
            'bank': hesabs,

        })
# -----------------------------------------------------------------------------------------------------------------------------------
    if (job != None) and (job != 'None') and (job != ''):
        personel = ''
        users = accuntmodel.objects.all()
        for user in users:
            if int(user.melicode) == int(operatormelicod):
                personel = user.firstname + ' ' + user.lastname

        jobarray = ['']
        jobarray.clear()
        ws = workmodel.objects.all()
        for w in ws:
            if int(w.melicodpersonel) == int(operatormelicod):
                et = "true"
                for ja in jobarray:
                    if ja[0] == w.work:
                        et = "false"
                if et == "true":
                    s = (w.work + "," + str(w.idjob)).split(",")
                    jobarray.append(s)
        detalarray = ['']
        detalarray.clear()
        jobs = ''
        if (job != None) and (job != ''):
            ws = workmodel.objects.all()
            for w in ws:
                if (w.idjob == job) and (w.hidde != 'hidde'):
                    p = ((w.detalework + ' ' + w.berand) + "," + str(w.id)).split(",")
                    detalarray.append(p)
            js = jobsmodel.objects.all()
            for j in js :
                if int(j.id) == int(job):
                    jobs = j.job
        for user in users:
            if user.melicode == melicode:
                name = user.firstname + " " + user.lastname
                etebarmelicod = "true"
        etebarbuttonsend = 'true'
        return render(request, 'reserv_reserver.html', context={
            'operatormelicod': operatormelicod,
            'melicode': melicode,
            'name': name,
            'etebarmelicod': etebarmelicod,
            'personel': personel,
            'jobs':jobarray,
            'detalarray':detalarray,
            'dayconter': dayconter,
            'jadid':jobs,
            'jid':job,
            'timesel':timesel,
            'bank': hesabs,
        })


    return render(request,'reserver.html', context={
        'dastiarray': dastiarray,
        'day': dayreserv,
        'operatorarray':operatorarray,
        'operatoreselect':operatoreselect,
        'dayconter': dayconter,
        'personel':personel,
        'melicodperonel':melicodperonel,
        'dayselect':dayselect,
        'mounthselect':mounthselect,
        'bank': hesabs,
        'e':e,
    })



    # users = accuntmodel.objects.all()
    # namedashbord = ''
    # dastrasi = ''
    # for user in users:
    #     if user.melicode == request.user.username:
    #         namedashbord = user.firstname + ' ' + user.lastname
    #         dastrasi = user.level
    #         if dastrasi == 'noshi':
    #             return render(request,'secretary_dashboard.html',context={})
    # tres =request.POST.get("tres")
    # timeselect = request.POST.get('timeselect')
    # karray = ['']
    # iunit = ['']
    # idkalaarray = ['']
    # berandkalaarray = ['']
    # if ( timeselect != None ) and ( timeselect != '' ):
    #     se = timeselect.split(",")
    #     reservs = reservemodel.objects.all()
    #     for reserv in reservs:
    #         if str(int(se[0])) == "41":
    #             if str(reserv.id) == str(int(se[1])):
    #                 n = ''
    #                 qs = accuntmodel.objects.all()
    #                 for q in qs:
    #                     if q.melicode == reserv.melicod:
    #                         n = q.firstname + " " + q.lastname
    #                 karray.clear()
    #                 workse = workmodel.objects.all()
    #                 for work in workse:
    #                     if int(reserv.idwork) == int(work.id):
    #                         jobs = jobsmodel.objects.all()
    #                         for job in jobs:
    #                             if int(work.idjob) == int(job.id):
    #                                 esmes = esmekalamodel.objects.all()
    #                                 for esme in esmes:
    #                                     if int(esme.jobid) == int(job.id):
    #                                         karray.append(esme.id)
    #
    #
    #         else:
    #             if reserv.personreserv == namedashbord:
    #                 if reserv.datemiladireserv == tres:
    #                     if int(se[0]) == int(reserv.numbertime) :
    #                         n = ''
    #                         qs = accuntmodel.objects.all()
    #                         for q in qs:
    #                             if q.melicode == reserv.melicod:
    #                                 n = q.firstname + " " + q.lastname
    #                         karray.clear()
    #                         workse = workmodel.objects.all()
    #                         for work in workse:
    #                             if int(reserv.idwork) == int(work.id):
    #                                 jobs = jobsmodel.objects.all()
    #                                 for job in jobs:
    #                                     if int(work.idjob) == int(job.id):
    #                                         esmes = esmekalamodel.objects.all()
    #                                         for esme in esmes:
    #                                             if int(esme.jobid) == int(job.id):
    #                                                 karray.append(esme.id)
    #     arrayselect = ['']
    #     arrayselect.clear()
    #     iunit = ['']
    #     idkalaarray = ['']
    #     iunit.clear()
    #     idkalaarray.clear()
    #     for i in range(int(len(karray))):
    #         s = "tickkala"+str(i)
    #         d = "valueunit"+str(i)
    #         # tickkala = request.POST.get(s)
    #         valueunit = request.POST.get(d)
    #         if (valueunit == '') or (valueunit == None):
    #             valueunit = '0'
    #         # if (tickkala != None) and (tickkala != ''):
    #         iunit.append(valueunit)
    #         idkalaarray.append(karray[int(i)])
    # dayconterstr = request.POST.get("dayconter")
    # button_next = request.POST.get("button_next")
    # button_back = request.POST.get("button_back")
    #
    # dayreserv = ['t']
    # dayreserv.clear()
    #
    #
    # t = datetime.datetime.now()
    # if (dayconterstr == None) or (dayconterstr == ""):
    #     dayconter = 0
    # else:
    #     dayconter = int(dayconterstr)
    # if button_next == 'accept' :
    #     dayconter += 1
    # if button_back == 'accept' :
    #     dayconter -= 1
    # if dayconter < 0 :
    #     dayconterm = dayconter * (-1)
    #     for i in range(dayconterm):
    #         t -= timedelta(days=1)
    # if dayconter > 0 :
    #     for i in range(dayconter):
    #         t += timedelta(days=1)
    #
    # dayarr = ['t']
    # dayarr.clear()
    # dayarr.append(stradb(t))
    # for h in range(41):
    #     dayarr.append('')
    # rs = reservemodel.objects.all()
    # name = ''
    # for r in rs:
    #     if (r.datemiladireserv == t.strftime('%a %d %b %y')) and (r.personreserv == namedashbord ) and (r.checking != 'true') :
    #         us = accuntmodel.objects.all()
    #         for u in us:
    #             if r.melicod == u.melicode :
    #                 name = u.firstname + " " + u.lastname
    #         dayarr[int(r.numbertime)] = name + " " + r.jobreserv + " " + r.detalereserv + " " + r.personreserv + " " + "بیعانه:" + " " + r.pyment
    #         i = 1
    #         while i < int(r.timereserv):
    #             dayarr[int(r.numbertime)+i] = "false"
    #             i += 1
    # dayreserv.append(dayarr)
    #
    # dastiarray = ['']
    # dastiarray.clear()
    # rs = reservemodel.objects.all()
    # for r in rs:
    #     if (r.datemiladireserv == t.strftime('%a %d %b %y')) and (r.personreserv == namedashbord ) and (r.numbertime == "41"):
    #         us = accuntmodel.objects.all()
    #         for u in us:
    #             if r.melicod == u.melicode :
    #                 name = u.firstname + " " + u.lastname
    #         dastiarray.append([(name + " " + r.jobreserv + " " + r.detalereserv + " " + r.personreserv + " " + "بیعانه:" + " " + r.pyment),str(r.id)])
    #
    #
    # reservid = request.POST.get("reservid")
    # fpezeshkibottom = request.POST.get("fpezeshkibottom")
    # vahedeobject = request.POST.get("vahedeobject")
    # vahedeobjectname = request.POST.get("vahedeobjectname")
    # description = request.POST.get("description")
    # if fpezeshkibottom == "accept" :
    #     ws = reservemodel.objects.all()
    #     for w in ws:
    #         cast = w.castreserv
    #         if int(w.id) == int(reservid) :
    #             if (vahedeobject != None) and (vahedeobject != ''):
    #                 cast = str(int(float(w.castreserv) * float(vahedeobject)))
    #             else:
    #                 vahedeobject = '1'
    #             fpeseshktestmodel.objects.create(
    #                 melicod=w.melicod,
    #                 jobreserv = w.jobreserv,
    #                 detalereserv = w.detalereserv,
    #                 personreserv = w.personreserv,
    #                 timereserv =w.timereserv,
    #                 castreserv =cast,
    #                 numbertime =w.numbertime,
    #                 hourreserv =w.hourreserv,
    #                 dateshamsireserv =w.dateshamsireserv,
    #                 datemiladireserv =w.datemiladireserv,
    #                 yearshamsi =w.yearshamsi,
    #                 cardnumber =w.cardnumber,
    #                 pyment =w.pyment,
    #                 trakingcod =w.trakingcod,
    #                 bank =w.bank,
    #                 checking =w.checking,
    #                 vahedeobject = vahedeobject,
    #                 vahedeobjectname = w.vahed,
    #                 reservid = reservid,
    #                 coment=description,
    #                 materiyal=idkalaarray,
    #                 valueunit=iunit,
    #                 bankpeyment=w.bankpeyment,
    #             )
    #             for z in range(len(idkalaarray)):
    #                 if (iunit[z] != '') and (iunit[z] != None):
    #                     anbars = anbarmodel.objects.all()
    #                     for ii in anbars:
    #                         if int(ii.kalaid) == int(idkalaarray[z]):
    #                             newvale = int(ii.value) - int(iunit[z])
    #                             a=anbarmodel.objects.filter(kalaid=str(ii.kalaid))
    #                             a.update(value=str(newvale))
    #
    #             a = reservemodel.objects.filter(id=int(reservid))
    #             a.delete()
    #             return redirect('/')
    #
    # if ( timeselect != None ) and ( timeselect != '' ):
    #     se = timeselect.split(",")
    #     reservs = reservemodel.objects.all()
    #     for reserv in reservs:
    #         if str(int(se[0])) == "41":
    #             if str(reserv.id) == str(int(se[1])):
    #                 n = ''
    #                 qs = accuntmodel.objects.all()
    #                 for q in qs:
    #                     if q.melicode == reserv.melicod:
    #                         n = q.firstname + " " + q.lastname
    #                 kalaarray = ['']
    #                 kalaarray.clear()
    #                 workse = workmodel.objects.all()
    #                 for work in workse:
    #                     if int(reserv.idwork) == int(work.id):
    #                         jobs = jobsmodel.objects.all()
    #                         for job in jobs:
    #                             if int(work.idjob) == int(job.id):
    #                                 esmes = esmekalamodel.objects.all()
    #                                 for esme in esmes:
    #                                     if int(esme.jobid) == int(job.id):
    #                                         a = ['']
    #                                         a.clear()
    #                                         a.append(esme.esmekala)
    #                                         a.append(esme.berand)
    #                                         a.append(esme.unit)
    #                                         a.append(esme.id)
    #                                         kalaarray.append(a)
    #                                         lenkalaarray = len(kalaarray)
    #
    #                 return render(request,'f1_pezeshk.html',context={
    #                     'name':n,
    #                     'procedure':reserv.jobreserv + " " + reserv.detalereserv,
    #                     'id':reserv.id,
    #                     'vahed':reserv.vahed,
    #                     'kalaarray': kalaarray,
    #                     'timeselect': timeselect,
    #                     'tres':tres,
    #                 })
    #         else:
    #             if reserv.personreserv == namedashbord:
    #                 if reserv.datemiladireserv == tres:
    #                     if int(se[0]) == int(reserv.numbertime) :
    #                         n = ''
    #                         qs = accuntmodel.objects.all()
    #                         for q in qs:
    #                             if q.melicode == reserv.melicod:
    #                                 n = q.firstname + " " + q.lastname
    #                         kalaarray = ['']
    #                         kalaarray.clear()
    #                         workse = workmodel.objects.all()
    #                         for work in workse:
    #                             if int(reserv.idwork) == int(work.id):
    #                                 jobs = jobsmodel.objects.all()
    #                                 for job in jobs:
    #                                     if int(work.idjob) == int(job.id):
    #                                         esmes = esmekalamodel.objects.all()
    #                                         for esme in esmes:
    #                                             if int(esme.jobid) == int(job.id):
    #                                                 a = ['']
    #                                                 a.clear()
    #                                                 a.append(esme.esmekala)
    #                                                 a.append(esme.berand)
    #                                                 a.append(esme.unit)
    #                                                 a.append(esme.id)
    #                                                 kalaarray.append(a)
    #                                                 lenkalaarray = len(kalaarray)
    #
    #                         return render(request,'f1_pezeshk.html',context={
    #                             'name':n,
    #                             'procedure':reserv.jobreserv + " " + reserv.detalereserv,
    #                             'id':reserv.id,
    #                             'vahed':reserv.vahed,
    #                             'kalaarray': kalaarray,
    #                             # 'lenkalaarray':lenkalaarray,
    #                             'timeselect':timeselect,
    #                             'tres': tres,
    #                         })
    #
    # return render(request,'dashbord.html',context={
    #                                                             'dastiarray':dastiarray,
    #                                                             'day': dayreserv,
    #                                                             'dayconter':dayconter,
    #                                                             't':t.strftime('%a %d %b %y')
    #                                                             })
def reservdasti(request):
    namepersonel = request.POST.get("namepersonel")
    job = request.POST.get("job")
    melicode = request.POST.get("melicode")
    detalework = request.POST.get("detalework")
    button_send = request.POST.get("button_send")
    castreserv = request.POST.get("castreserv")
    personreserv = request.POST.get("personreserv")
    namebuttom = request.POST.get('namebuttom')
    names =request.POST.get("names")
    tickon = request.POST.get("tickon")
    detalework = request.POST.get("detalework")
    pey = request.POST.get("pey")
    bankpey = request.POST.get("bankpey")
    if (pey == '') or (pey == None):
        pey = '0'
        bankpey = '-2'
    yu = int(bankpey)

    # ------تولید لیست حسابهای بانکی در hesabs-و کار انتخاب شده رو میریزه توی b----
    banks = bankmodel.objects.all()
    hesabs = [""]
    hesabs.clear()
    for bank in banks:
        r = 0
        for hesab in hesabs :
            if hesab[1] ==  bank.onvan :
                r = 1
        if r == 0 :
            s = (str(bank.id )+ "," + str(bank.onvan)).split(",")
            hesabs.append(s)

# --------------------------------------------------------------------------------

    arrayname =['']
    if namebuttom == 'accept':
        ls = searchmodeltest.objects.all()
        for l in ls:
            a = searchmodeltest.objects.filter(m=l.m)
            a.delete()
        arrayname.clear()

        auser = accuntmodel.objects.all()
        amaray = ['']
        amaray.clear()
        for uss in auser:
            if uss.firstname[0:3] == names :
                mm = ['']
                mm.clear()
                mm.append(uss.firstname + " " + uss.lastname)
                mm.append(uss.melicode)
                amaray.append(uss.melicode)
                searchmodeltest.objects.create(m=uss.melicode)
                arrayname.append(mm)
        for aa in auser:
            if aa.lastname[0:3] == names :
                cheek = "true"
                for archek in amaray:
                    if archek == aa.melicode :
                        cheek = "false"
                if cheek == "true" :
                    mm = ['']
                    mm.clear()
                    mm.append(aa.firstname + " " + aa.lastname)
                    mm.append(aa.melicode)
                    searchmodeltest.objects.create(m=aa.melicode)
                    arrayname.append(mm)
        return render(request,'reserv_dasti.html',context={
            'arrayname':arrayname,
            'bank': hesabs,

        })

    ls = searchmodeltest.objects.all()
    if (tickon != None) and (tickon != ''):
        inttikon = int(tickon)
        ar = ['']
        ar.clear()
        for l in ls :
            ar.append(l.m)
                           # -- چون سرور بر عکس ترتیه ها رو میخونه ایمچا و در cash viwo . cast این کامنت هست-
        ar.reverse()
        melicode = ar[inttikon]





    etebarmelicod = "notr"
    if melicode == None:
        melicode = ''
    users = accuntmodel.objects.all()
    name = ''
    if (melicode != None) and (melicode != ''):
        etebarmelicod = "false"
        for user in users:
            if user.melicode == melicode:
                name = user.firstname + " " + user.lastname
                etebarmelicod = "true"

    namepersonal = ['']
    namepersonal.clear()
    ws = workmodel.objects.all()
    for w in ws:
        t = "true"
        for n in namepersonal:
            if w.melicodpersonel == n[0]:
                t = 'false'
        if t == 'true' :
            users = accuntmodel.objects.all()
            for user in users:
                if user.melicode == w.melicodpersonel :
                    p = (w.melicodpersonel + "," + str(user.firstname + ' ' + user.lastname)).split(",")
                    namepersonal.append(p)


    personel = ''
    users = accuntmodel.objects.all()
    for user in users:
        if user.melicode == namepersonel:
            personel = user.firstname + ' ' + user.lastname
    jobarray = ['']
    jobarray.clear()
    ws = workmodel.objects.all()
    for w in ws:
        if w.melicodpersonel == namepersonel:
            et = "true"
            for ja in jobarray:
                if ja[0] == w.work:
                    et = "false"
            if et == "true":
                s = (w.work + "," + str(w.idjob)).split(",")
                jobarray.append(s)
    detalarray = ['']
    detalarray.clear()
    if ( job != None ) and ( job != ''):
        ws = workmodel.objects.all()
        for w in ws:
            if (w.idjob == job)  and (w.hidde != 'hidde'):
                p = ((w.detalework + ' ' + w.berand)+","+str(w.id)).split(",")
                detalarray.append(p)

    etebarreservdasti = 'notr'
    if button_send == 'accept':
        numbertime = '41'
        hourreserv = 'timeout'
        dateshamsireserv = stradby(dt.now())
        datemiladireserv = dt.now().strftime('%a %d %b %y')
        yearshamsi = stry(dt.now())
        ws = workmodel.objects.all()
        timereserv = "0"
        vahed = ''
        d = '0'
        jj = ''
        for w in ws:
            if str(w.id) == str(detalework):
                personreserv = w.person
                castreserv = w.cast
                d = w.detalework
                vahed = w.vahed
                jj = w.work
        etebarreservdasti = 'true'
        reservemodel.objects.create(
            melicod= melicode,
            jobreserv = jj,
            detalereserv = d,
            personreserv = personreserv,
            timereserv = timereserv,
            castreserv = castreserv,
            numbertime = numbertime,
            hourreserv = hourreserv,
            dateshamsireserv = dateshamsireserv,
            datemiladireserv = datemiladireserv,
            yearshamsi = yearshamsi,
            vahed=vahed,
            idwork=detalework,
            pyment = pey,
            bankpeyment=bankpey,
        )

    return render(request,'reserv_dasti.html',context={
        'jobs':jobarray,
        'melicode':melicode,
        'job':job,
        'detalarray':detalarray,
        'personreserv':personreserv,
        'castreserv':castreserv,
        'etebarmelicod':etebarmelicod,
        'name':name,
        'etebarreservdasti':etebarreservdasti,
        'namepersonal':namepersonal,
        'personel':personel,
        'melipersonel':namepersonel,
        'bank': hesabs,

    })


# ---------------------------------------------------مرخصی-----------------------------------------
# --------------------------------------------------------------------------------------------
def leave(request):
    context={'user' : request.user.username}
    return render(request,'new_leave.html',context)

@csrf_exempt
def new_timeleav_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            selected_date = data.get('selected_date')
            nationalcode = data.get('nationalcode')
            day = data.get('day')
            timeselect = data.get('time')

            # اعتبارسنجی داده‌های ورودی
            if not nationalcode:
                return JsonResponse({'error': 'کد ملی الزامی است'}, status=400)

            if timeselect:
                timeselect = int(timeselect)
                if timeselect < 1 or timeselect > 40:
                    return JsonResponse({'error': 'زمان انتخاب شده نامعتبر است'}, status=400)

            if day:
                day = int(day)
                if day < 1 or day > 30:
                    return JsonResponse({'error': 'روز انتخاب شده نامعتبر است'}, status=400)

            # پردازش درخواست
            reserved_times = []
            rar = []

            if timeselect and day:
                reserved_times = listleav(day, timeselect, nationalcode)
                rar = timebeforreserv(day,nationalcode)

            elif selected_date:
                reserved_times = listleav(selected_date, None, nationalcode)
                rar = timebeforreserv(selected_date,nationalcode)
            elif day:
                reserved_times = listleav(day, None, nationalcode)
                rar = timebeforreserv(day,nationalcode)

            # reserved_times = [5,6,7]
            # rar = [1,2,3]
            return JsonResponse({'reserved_times': reserved_times,
                                 'rar': rar
                                 })

        except json.JSONDecodeError:
            return JsonResponse({'error': 'داده‌های ارسالی نامعتبر است'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    # حالت GET
    default_date = dt.now() + timedelta(days=2)
    jalali_date = convert(default_date)
    context = {
        'melicode': request.user.username,
    }
    return render(request, 'new_timereserv.html', context)

@csrf_exempt

def listleav(dayy, timeselect, nationalcode):
    try:
        # محاسبه تاریخ
        select_day_date = dt.now() + timedelta(days=int(dayy) + 1)
        dateleav = stry(select_day_date) + strbadd(select_day_date) + strd(select_day_date)

        # تبدیل به عدد صحیح
        nationalcode = int(nationalcode)

        # مدیریت زمان‌ها
        if timeselect is not None:
            time_index = int(timeselect) - 1  # تبدیل به اندیس 0-39

            # بررسی وجود رکورد
            try:
                record = leavemodel.objects.get(
                    personelmelicod=nationalcode,
                    date=dateleav
                )
                current_times = [int(t.strip()) for t in record.leave.split(',') if t.strip()]

                # Toggle وضعیت مرخصی
                if time_index in current_times:
                    current_times.remove(time_index)
                else:
                    current_times.append(time_index)

                record.leave = ','.join(map(str, sorted(current_times)))
                record.save()

            except leavemodel.DoesNotExist:
                # ایجاد رکورد جدید
                leavemodel.objects.create(
                    personelmelicod=nationalcode,
                    date=dateleav,
                    leave=str(time_index)
                )
                current_times = [time_index]

            return sorted(current_times)

        else:
            # فقط دریافت لیست
            try:
                record = leavemodel.objects.get(
                    personelmelicod=nationalcode,
                    date=dateleav
                )
                return sorted([int(t.strip()) for t in record.leave.split(',') if t.strip()])
            except leavemodel.DoesNotExist:
                return []

    except Exception as e:
        print(f"Error in listleav: {str(e)}")
        raise

@csrf_exempt
def finalize_leave(request):
    # انجام عملیات نهایی و اعتبارسنجی
    # ...
    return JsonResponse({'status': 'success'})

# نمایش داشبورد منشی-------------------------------------------------------------------------------------------------------
def dashborddef(request):
    return render(request, 'secretary_dashboard.html')


@csrf_exempt
def search_members(request):
    query = request.GET.get('q', '').strip()

    if len(query) < 2:
        return JsonResponse({'members': []})

    members = accuntmodel.objects.filter(
        Q(firstname__icontains=query) |
        Q(lastname__icontains=query) |
        Q(melicode__icontains=query) |
        Q(phonnumber__icontains=query)
    ).values('id', 'firstname', 'lastname', 'melicode', 'phonnumber')[:10]

    return JsonResponse({'members': list(members)})


@csrf_exempt
def member_profile(request):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        if not member_id:
            return redirect('/reserv/dashboard/')

        try:
            member = accuntmodel.objects.get(id=member_id)
            context = {'member': member}
            return render(request, 'member_profile.html', context)
        except accuntmodel.DoesNotExist:
            return redirect('/reserv/dashboard/')
    return redirect('/reserv/dashboard/')


@csrf_exempt
def cashier_view(request):
    # دریافت member_id از session
    member_id = request.session.get('cashier_member_id')

    if not member_id:
        return redirect('secretary_dashboard')

    try:
        member = accuntmodel.objects.get(id=member_id)
        # فقط خدمات پرداخت نشده را فیلتر می‌کنیم (cheking=False)
        services = fpeseshktestmodel.objects.filter(melicod=member.melicode, checking = 'false')

        banks = bankmodel.objects.all()
        # محاسبه قیمت هر سرویس و مبالغ قابل پرداخت
        total_service = 0
        total_discount = 0
        total_advance = 0

        for service in services:
            try:
                # تبدیل مقادیر به عدد
                castreserv = int(service.castreserv) if service.castreserv and service.castreserv.isdigit() else 0
                vahedeobject = int(
                    service.vahedeobject) if service.vahedeobject and service.vahedeobject.isdigit() else 1
                offer = int(service.offer) if service.offer and service.offer.isdigit() else 0
                pyment = int(service.pyment) if service.pyment and service.pyment.isdigit() else 0

                # محاسبات
                service_total = castreserv * vahedeobject
                total_service += service_total
                total_discount += offer
                total_advance += pyment

                # ذخیره در آبجکت برای استفاده در تمپلیت
                service.calculated_total = service_total
                service.calculated_offer = offer
                service.calculated_pyment = pyment
                service.payable_amount = service_total - offer - pyment

            except Exception as e:
                service.calculated_total = 0
                service.calculated_offer = 0
                service.calculated_pyment = 0
                service.payable_amount = 0

        total_payable = total_service - total_discount - total_advance

        # تبدیل به حروف
        def rial_to_toman_words(amount):
            try:
                toman = amount // 10
                return num2words(toman, lang='fa') + " تومان"
            except:
                return ""

        total_payable_words = rial_to_toman_words(total_payable)
        # تبدیل تخفیف به تومان و حروف برای هر سرویس
        for service in services:
            service.offer_toman = service.calculated_offer // 10
            service.offer_words = num2words(service.offer_toman, lang='fa') + " تومان"

        # آماده‌سازی بانک‌ها برای جاوااسکریپت
        banks_json = serialize('json', banks)

        context = {
            'member': member,
            'services': services,
            'banks': banks,
            'total_service': total_service,
            'total_discount': total_discount,
            'total_advance': total_advance,
            'total_payable': total_payable,
            'total_payable_words': total_payable_words,
            'banks_json': banks_json,
        }
        return render(request, 'cashier.html', context)
    except accuntmodel.DoesNotExist:
        return redirect('secretary_dashboard')
    except Exception as e:
        return redirect('secretary_dashboard')


@csrf_exempt
def update_advance(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            service_id = data.get('service_id')
            advance_amount = data.get('advance_amount')
            bank_id = data.get('bank_id')

            service = fpeseshktestmodel.objects.get(id=service_id)
            bank = bankmodel.objects.get(id=bank_id)

            service.pyment = str(advance_amount)
            service.bankpeyment = str(bank.id)
            service.save()

            return JsonResponse({
                'status': 'success',
                'new_advance': advance_amount,
                'bank_name': bank.onvan
            })
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error'}, status=400)


@csrf_exempt
def start_cashier_session(request):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        if not member_id:
            return redirect('secretary_dashboard')

        # ذخیره member_id در session
        request.session['cashier_member_id'] = member_id
        return redirect('cashier_view')
    return redirect('secretary_dashboard')


@csrf_exempt
def submit_payment(request):
    if request.method == 'POST':
        member_id = request.session.get('cashier_member_id')
        if not member_id:
            return redirect('secretary_dashboard')

        try:
            member = accuntmodel.objects.get(id=member_id)
            # تاریخ‌های شمسی و میلادی
            now = dt.now()
            date_shamsi = jdatetime.datetime.fromgregorian(datetime=now).strftime('%Y/%m/%d')
            date_miladi = now.strftime('%Y-%m-%d')

            # پردازش تخفیف‌ها
            for service in services:
                discount_key = f'discount_{service.id}'
                new_discount = request.POST.get(discount_key, service.offer)

                if new_discount != service.offer:
                    service.offer = new_discount
                    service.save()

            # پردازش پرداخت‌ها
            payments = json.loads(request.POST.get('payments', '[]'))
            paid_service_ids = []

            for payment in payments:
                service_id = payment['service_id']
                amount = payment['amount']
                bank_id = payment['bank_id']

                service = fpeseshktestmodel.objects.get(id=service_id)
                bank = bankmodel.objects.get(id=bank_id)

                # ایجاد رکورد پرداخت
                castmodel.objects.create(
                    idf=str(service.id),
                    melicodvarizande=member.melicode,
                    dateshamsi=date_shamsi,
                    datemiladi=date_miladi,
                    mablagh=str(amount),
                    bankpeyment=str(bank.id),
                    filenumber='0',
                    cashmethodname='0',
                    cashmethodid='0',
                    melicodeoperatore='0',
                    dateshamsieditor='0'
                )

                # علامت گذاری سرویس به عنوان پرداخت شده
                service.cheking = True
                service.save()
                paid_service_ids.append(service_id)

            # حذف session پس از تکمیل پرداخت
            if 'cashier_member_id' in request.session:
                del request.session['cashier_member_id']

            return redirect('member_profile', member_id=member_id)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return redirect('cashier_view')




from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def submit_deposit(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            deposit_amount = data.get('deposit_amount')
            print("مبلغ بیعانه دریافت‌شده:", deposit_amount)  # در ترمینال چاپ میشه
            return JsonResponse({'status': 'success', 'message': 'پرداخت بیعانه ثبت شد'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'خطا در پردازش داده‌ها'})
    return JsonResponse({'status': 'error', 'message': 'درخواست نامعتبر'})
# ----------------------------------------------------------------------------------------
# reservations/views.py

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
import json
import logging

logger = logging.getLogger(__name__)

def reservation_summary(request):
    context = {
        'work': 'خدمت نمونه',
        'detalework': 'جزئیات خدمت',
        'personwork': 'اپراتور نمونه',
        'dateshamsi': '۱۴۰۳/۰۳/۲۲',
        'hoursreserv': '۱۴:۳۰',
        'banks': [
            {'id': 1, 'onvan': 'بانک ملت - ۱۲۳۴'},
            {'id': 2, 'onvan': 'بانک صادرات - ۵۶۷۸'},
        ]
    }
    return render(request, 'new_reserv_end.html', context)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def save_reserv_profiles(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            action = data.get('action')
            # بخش ثبت بیعانه
            if action == 'deposit':
                amount = data.get('amount')
                bank_id = data.get('bank_id')
                # ذخیره مبلغ در session برای استفاده بعدی
                request.session['deposit_amount'] = amount
                request.session['bank_id'] = bank_id


                # TODO: ذخیره‌سازی در مدل‌های شما
                return JsonResponse({
                    'success': True,
                    'message': f'بیعانه {amount} ریال ثبت شد'
                })

            # بخش ثبت نهایی رزرو
            elif action == 'finalize':
                # دریافت مبلغ بیعانه از session
                deposit_amount = request.session.get('deposit_amount')
                procedureselect = request.session.get('selected_option_id')
                melicod = request.session.get('national_code')
                amount = request.session.get('amount')
                selected_day = request.session.get('selected_day')
                selected_time = request.session.get('selected_time')
                select_day_date = dt.now()
                try:
                    select_day_date += timedelta(days=int(selected_day) + 1)
                except:
                    a = 1
                request.session['dateshamsireserv'] = stradb(select_day_date)
                request.session['datemiladireserv'] = select_day_date.strftime('%a %d %b %y')
                request.session['yearshamsi'] = stry(dt.now())
                request.session['numbertime'] = selected_time

                # TODO: عملیات نهایی‌سازی رزرو
                works = workmodel.objects.all()
                j = ''
                d = ''
                p = ''
                t = ''
                c = ''
                f = ''
                ll = ''
                p = ''
                v = ''

                for work in works:
                    if work.id == int(procedureselect) :
                        j = work.work
                        d = work.detalework
                        p = work.melicodpersonel
                        c = work.cast
                        v = work.vahed
                        if work.time == "زمان کمی میبرد":
                            t = "0"
                            selectprocedure.append("0")
                        if work.time == "پانزده دقیقه":
                            t = "1"
                            selectprocedure.append("1")
                        if work.time == "سی دقیقه":
                            t = "2"
                            selectprocedure.append("2")
                        if work.time == "چهل و پنج دقیقه":
                            t = "3"
                            selectprocedure.append("3")
                        if work.time == "یک ساعت":
                            t = "4"
                            selectprocedure.append("4")
                        if work.time == "یک ساعت و پانزده دقیقه":
                            t = "5"
                            selectprocedure.append("5")
                        if work.time == "یک ساعت و نیم":
                            t = "6"

                users = accuntmodel.objects.all()
                for user in users:
                    if int(user.melicode) == int(request.session['national_code']):
                        f = user.firstname
                        ll = user.lastname
                        ph = user.phonnumber
                #
                #
                reservemodel.objects.create(
                melicod = melicod,
                vaziyatereserv = 'هماهنگی روز قبل انجام نشده است' ,
                jobreserv = j,
                detalereserv = d,
                personreserv = p,
                timereserv = t,
                castreserv = c,
                numbertime = request.session['selected_time'],
                hourreserv = request.session['hourreserv'],
                dateshamsireserv = stradb(select_day_date),
                datemiladireserv = select_day_date.strftime('%a %d %b %y'),
                yearshamsi = stry(select_day_date),
                # cardnumber = models.CharField(max_length=20, default='0')
                pyment = request.session.get('deposit_amount'),
                # trakingcod = models.CharField(max_length=20, default='0')
                # bank =
                # checking = models.CharField(max_length=20, default='false')
                vahed = v,
                idwork = str(procedureselect),
                bankpeyment = request.session.get('bank_id'),
                )

                request.session['deposit_amount'] = 0
                request.session['bank_id'] = 'بیعانه پرداخت نشده است'
                return JsonResponse({
                    'success': True,
                    'message': 'رزرو با موفقیت ثبت شد'
                })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)

    return JsonResponse({
        'success': False,
        'error': 'عملیات نامعتبر'
    }, status=400)


def reserv_profile(request):
    # TODO: پیاده‌سازی صفحه پروفایل رزرو
    pass

# def reserv_profile(request):
#     # TODO: پیاده‌سازی صفحه پروفایل رزرو
#     pass