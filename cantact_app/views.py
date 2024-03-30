from django.shortcuts import render , redirect
import tkinter
from tkinter import messagebox
import datetime
from jalali_date import date2jalali,datetime2jalali
from datetime import timedelta
from cantact_app.models import accuntmodel,savecodphon,dataacont
from cantact_app.forms import accuntform
from kavenegar import *
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout



import matplotlib
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
def cuntmounth(x):
    w = ""
    if x == 1 :
        w = "فروردین"
    if x == 2 :
        w = "اردیبهشت"
    if x == 3 :
        w = "خرداد"
    if x == 4 :
        w = "تیر"
    if x == 5 :
        w = "مرداد"
    if x == 6 :
        w = "شهریور"
    if x == 7 :
        w = "مهر"
    if x == 8 :
        w = "آبان"
    if x == 9 :
        w = "آذر"
    if x == 10 :
        w = "دی"
    if x == 11 :
        w = "بهمن"
    if x == 12 :
        w = "اسفند"
    return (w)


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
def stryabd(tdef):
    r = stry(tdef)+' '+stra(tdef)+' '+strb(tdef)+' '+strd(tdef)
    return (r)
def stryadb(tdef):
    r = stry(tdef)+' '+stra(tdef)+' '+strd(tdef)+' '+strb(tdef)
    return (r)
def strn():
    tx = datetime.datetime.now()
    r = stry(tx)+' '+stra(tx)+' '+strd(tx)+' '+strb(tx)
    return (r)
def strbd(tdef):
    r = strb(tdef)+' '+strd(tdef)
    return (r)

t = [datetime.datetime.now()]
t[0] = datetime.datetime.now()
# year = [int(str('14' + stry(datetime.datetime.now())))]
# year[0] = []
# year[0] =int(str('14' + stry(datetime.datetime.now())))
calandarshow = ['0']
calandarshow[0] ='0'
calandarmiladidate = [datetime.datetime.now()]
calandarmiladidate[0] = datetime.datetime.now()
calandarshamsidate = [stradby(t[0])]
calandarshamsidate [0] = stradby(t[0])
firstname_r = ['']
lastname_r = ['']
melicod_r = ['']
phonnumber_r = ['']
berthmiladi_r = [datetime.datetime.now()]
berthmiladi_r[0] = datetime.datetime.now()
melicod_etebar = ['true']
mounth_number = ['']
year = [1402]
def addcantactdef(request):
    mounth_number[0] = request.POST.get('mbtn')
    if mounth_number[0] == None :
        mounth_number[0] == ''
    bbtn = request.POST.get("bbtn")
    button_upmounth = request.POST.get("button_upmounth")
    button_downmounth = request.POST.get("button_downmounth")
    button_calandar = request.POST.get("button_calandar")
    button_back = request.POST.get("button_back")
    button_send = request.POST.get('button_send')
    buttoncode_repeat = request.POST.get('buttoncode_repeat')
    buttoncode_send = request.POST.get('buttoncode_send')
    inputcode_regester = request.POST.get('inputcode_regester')
    formuser = accuntform(request.POST, request.FILES)
    facebotton = request.POST.get("facebutton")
    yearj = request.POST.get("year")
    mounthj = request.POST.get("mounth")
    dayj = request.POST.get("day")
# ---------- در این قسمت داده هایی که به صفحه addcontact داده میشود در آرایه هایدمربوطه ذخیره میشه تا با زدن دکمه ها اونا نپرن ----
    input_year = request.POST.get("input_year")
    if (input_year != '') and ( input_year != None) :
        year[0] = input_year

    # ------اگر ماه رو اشتباه وارد کرده باشه و بخواد ماه رو عوض کنه روی ماه میزنه و سال صفر میشه د دوباره کلید تقویم میخورد و همه جی از اول-----
    mounthbtn = request.POST.get("mounthbtn")
    if mounthbtn == "accept":
        button_calandar = "accept"
        year[0] = []

    firstname = request.POST.get("firstname")
    if (firstname != '') and ( firstname != None) :
        firstname_r[0] = firstname
    if firstname_r[0] == None :
        firstname_r[0] = ''

    lastname = request.POST.get("lastname")
    if (lastname != '') and ( lastname != None) :
        lastname_r[0] = lastname
    if lastname_r[0] == None :
        lastname_r[0] = ''


    melicod_etebar[0] = 'f'
    melicod = request.POST.get("melicod")

    if (melicod != '') and ( melicod != None) :
        melicod_etebar[0] = 'true'

        users = accuntmodel.objects.all()
        for user in users :
            if user.melicode == melicod :
                melicod_etebar[0] = 'false'
        melicod_r[0] = melicod

    if melicod_r[0] == None :
        melicod_r[0] = ''

    phonnumber = request.POST.get("phonnumber")
    if (phonnumber != '') and ( phonnumber != None) :
        phonnumber_r[0] = phonnumber
    if phonnumber_r[0] == None :
        phonnumber_r[0] = ''

# --------پس از وارد کردن یک عدد چهار رقمی در باکس سال توسط جاوا دکمه battonface زده میشود در این قسمت میگوید اگر اگر زده شد یعتی سال وارد شده و پس جدول ماهها باز شور---------
    if facebotton == "accept":
        mounth_number[0] = "0"
        return render(request,'calander.html',context={
                                                       "firstname":firstname_r[0],
                                                       "lastname":lastname_r[0],
                                                       "melicod":melicod_r[0],
                                                       "phonnumber":phonnumber_r[0],
                                                        "year" : year[0],
                                                        "mounth": mounth_number[0],
                                                        "calandar_aray":calandarshow,
                                                       })

# -------اینجا وقتی یک ماه انتخاب میشه میاد و جدول هفته اون رو مشخص میکنه------------------------------------------------------------------------------
#     if (mounth_number[0] != '') and (mounth_number[0] != "0") and (mounth_number[0] != None):
#         time = datetime.datetime.now()
#         q = '14'
#         while int(str(q + stry(time))) >= int(str(year[0])) :
#             time -= timedelta(days=30)
#             if stry(time) == '99' :
#                 q = '13'
#         while int(str(q + stry(time))) == int(str(year[0])) :
#             time += timedelta(days=1)
#
#         while strb(time) != cuntmounth(int(mounth_number[0])) :
#             time += timedelta(days=1)
#
#         calandarshow.clear()
#         calandarmiladidate.clear()
#         calandarshamsidate.clear()
#         i = 0
#         if stra(time) == "شنبه" :
#             i = 1
#         if stra(time) == "یکشنبه" :
#             i = 2
#         if stra(time) == "دوشنبه" :
#             i = 3
#         if stra(time) == "سه‌شنبه" :
#             i = 4
#         if stra(time) == "چهارشنبه" :
#             i = 5
#         if stra(time) == "پنج‌شنبه" :
#             i = 6
#         if stra(time) == "جمعه" :
#             i = 7
#         for j in range(i):
#             time -= timedelta(days=1)
#         for j in range(i) :
#             calandarshow.append("")
#             calandarmiladidate.append(time)
#             calandarshamsidate.append(stradby(time))
#             time += timedelta(days=1)
#
#         while strb(time) == cuntmounth(int(mounth_number[0])) :
#             calandarshow.append(strd(time))
#             calandarmiladidate.append(time)
#             calandarshamsidate.append(stradby(time))
#             time += timedelta(days=1)
#         for i in range(len(calandarshamsidate)) :
#             w = calandarshamsidate[i]
#         return render(request,'calander.html',context={"firstname":firstname_r[0],
#                                                        "lastname":lastname_r[0],
#                                                        "melicod":melicod_r[0],
#                                                        "phonnumber":phonnumber_r[0],
#                                                         "year" : year[0],
#                                                         "mounth":cuntmounth(int(mounth_number[0])),
#                                                         "calandar_aray":calandarshow,
#                                                        })
#
# ---------اگر دکمه تقئیم خورد سال رو به هم اکنون تغییر میده دقت شود که در مواد دیگه مثل بالا زدن-سال یا چیزی دیگه - button calandar برابر acceot میشد-----------------------------------متوجه شدم که placeholder-مقدارش داخل input خواهد بود----------------------------------------------------------------
#     if button_calandar == "accept" :
#         t[0] = datetime.datetime.now()
#         calandarshow[0] = '0'
#         calandarmiladidate[0] = datetime.datetime.now()
#         calandarshamsidate[0] = stradby(t[0])
#         berthmiladi_r[0] = datetime.datetime.now()
#         year[0] = []
#         return render(request, 'calander.html', context={"firstname": firstname_r[0],
#                                                  "lastname": lastname_r[0],
#                                                  "melicod": melicod_r[0],
#                                                  "phonnumber": phonnumber_r[0],
#                                                  "year": year[0],
#                                                  "mounth": mounth_number[0],
#                                                  "calandar_aray": calandarshow,
#                                                  })
# # ****************************************************کلید برگشت**********************************************
    if button_back == "accept" :
        melicod_r[0] = ''
        return redirect('"http://127.0.0.1:8000"')
# -----------------------------------------------------------------انتخاب روز تولد----------------------------------------------
#     if (bbtn != None) and (bbtn != '') and (calandarshow != None) and (calandarshow != '') :
#         # berthmiladi_r[0] = str(calandarmiladidate[int(bbtn)])
#         year[0] = []
#         return render(request,'add_cantact.html',context={ "firstname":firstname_r[0],
#                                                            "lastname":lastname_r[0],
#                                                            "melicod":melicod_r[0],
#                                                            "phonnumber":phonnumber_r[0],
#                                                            "year" : year[0],
#                                                            "berthday_shamsi":calandarshamsidate[int(bbtn)],
#                                                            "melicod_etebar": 'true',
#                                                            })
# ------------------------------------------------بعد از زدن دکمه ارسال در صفحه add_cantact- و یا بعد از زدن دکمه ارسال مجدد----کد ارسال میکنخ با پیامک-------------------------
    if (button_send == 'accept') or (buttoncode_repeat == 'accept'):
        if (melicod_r[0] == '') and (melicod_r[0] == None)  :
            melicod_etebar[0] = 'empty'
        if melicod_etebar[0] == 'true' :
            savecods = savecodphon.objects.all()
            for savecode in savecods:
                a = savecodphon.objects.filter(melicode=savecode.melicode)
                a.delete()
            randomcode = random.randint(1000, 9999)
            savecodphon.objects.create(firstname=firstname_r[0], lastname=lastname_r[0],melicode=str(melicod_r[0]),
                                       phonnumber=str(phonnumber_r[0]),
                                       berthdayyear =str(yearj),
                                       berthdayday=str(dayj),
                                       berthdaymounth=str(mounthj),
                                       code=str(randomcode),
                                       expaiercode="2",
                                       )
            try:
                api = KavenegarAPI(
                    '527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D')
                params = {
                    'receptor': phonnumber_r[0],
                    'template': 'test',
                    'token': randomcode,
                    'type': 'sms',
                    }
                response = api.verify_lookup(params)
                return render(request, 'code_cantact.html')
            except APIException as e:
                m = 'tellerror'
                return render(request, 'add_cantact.html', context={'melicod_etebar': m})
            except HTTPException as e:
                m = 'neterror'
                return render(request, 'add_cantact.html', context={'melicod_etebar': m}, )

            #     return render(request, 'code_cantact.html')
            # except APIException as e:
            #     # messages.error(request,'در سیستم ارسال پیامک مشکلی پیش آمده لطفا شماره خود را به درستی وارد کنید و دوباره امتحان کنید در صورتی که مشکل برطرف نشد در اینستاگرام پیام دهید ')
            #     return render(request, 'add_cantact.html')
            # except HTTPException as e:
            #     # messages.error(request,'در سیستم ارسال پیامک مشکلی پیش آمده لطفا شماره خود را به درستی وارد کنید و دوباره امتحان کنید در صورتی که مشکل برطرف نشد در اینستاگرام پیام دهید ')
            #     return render(request, 'add_cantact.html')
            #

        else :
            year[0] = []
            yearcant = [1300]
            h = 1300
            t = datetime.datetime.now()
            while h <= int(stry(t)) + 1399:
                h += 1
                yearcant.append(h)
            day = [1]
            hh = 1
            while hh <= 30:
                hh += 1
                day.append(hh)

            return render(request, 'add_cantact.html', context={
                                                                'melicod_etebar': melicod_etebar[0],
                                                                "yearcant": yearcant,
                                                                "day": day,
                                                                "firstname": firstname_r[0],
                                                                "lastname": lastname_r[0],
                                                                "melicod": melicod_r[0],
                                                                "phonnumber": phonnumber_r[0],
                                                            })

# --------------------------------------------------------------------------------------------------------------------------------
    if (buttoncode_send != None) and (buttoncode_send != '') and (inputcode_regester != None) and (inputcode_regester != ''):
        savecods = savecodphon.objects.all()
        for savecode in savecods :
            if int(savecode.code) == int(inputcode_regester):
                yj = savecode.berthdayyear
                dj = savecode.berthdayday
                mj = savecode.berthdaymounth
                time = datetime.datetime.now()
                q = '14'
                while int(str(q + stry(time))) >= int(yj):
                    time -= timedelta(days=30)
                    if int(stry(time)) == int('99'):
                        q = '13'
                while int(str(q + stry(time))) == int(yj):
                    time += timedelta(days=1)
                while strb(time) != mj:
                    time += timedelta(days=1)
                while int(strd(time)) != int(dj):
                    time += timedelta(days=1)


                accuntmodel.objects.create(
                                firstname=savecode.firstname,
                                lastname=savecode.lastname,
                                melicode=savecode.melicode,
                                phonnumber=savecode.phonnumber,
                                berthday=stradby(time),
                                pasword=savecode.phonnumber,
                                )
                a = savecodphon.objects.filter(melicode=savecode.melicode)
                a.delete()

                User.objects.create_user(
                                                username=savecode.melicode,
                                                password=savecode.phonnumber,
                                                first_name=savecode.firstname,
                                                last_name=savecode.lastname,
                                            )

                user_login =authenticate(request,
                                             username=savecode.melicode,
                                             password=savecode.phonnumber,
                                             )

                login (request,user_login)
                e = 'succes'
                return render(request,'code_cantact.html',context={'etebar':e},)
                        # return redirect('/')
            # return render(request, 'cod_of_phon.html')
            else:
                e = 'false'
                return render(request, 'code_cantact.html', context={'etebar': e}, )
    year[0] = []
    yearcant = [1300]
    h =1300
    t = datetime.datetime.now()
    while h <= int(stry(t))+1399 :
        h +=1
        yearcant.append(h)
    day = [1]
    hh = 1
    while hh <= 30 :
        hh +=1
        day.append(hh)

    return render(request,'add_cantact.html',context={'melicod_etebar':melicod_etebar[0],
                                                                    "yearcant":yearcant,
                                                                    "day":day,
                                                                    })
login_etebar = ['f']


def logindef(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    button_back = request.POST.get("button_back")
    button_send = request.POST.get("button_send")
    login_etebar[0] = 'f'
    if button_back == 'accept' :
        return redirect('/')
    if button_send == 'accept' :
        login_etebar[0] = 'false'
        if (username == '' ) or (username == None):
            login_etebar[0] = 'empty'
        users = accuntmodel.objects.all()
        for user in users :
            if username == user.melicode :
                login_etebar[0] = 'false_in_paswoord'
                if password == user.pasword :
                    login_etebar[0] = 'true'
                    a = User.objects.filter(username=username)
                    a.delete()
                    User.objects.create_user(
                                                username=user.melicode,
                                                password=user.pasword,
                                                first_name=user.firstname,
                                                last_name=user.lastname,
                                            )

                    user_login =authenticate(request,
                                             username=user.melicode,
                                             password=user.pasword,
                                             )
                    if user_login is not None:
                        login(request, user_login)
                        # return redirect('/')
    return render(request,'login_cantact.html',context={
                                                                    "firstname": firstname_r[0],
                                                                    "lastname": lastname_r[0],
                                                                    "melicod": melicod_r[0],
                                                                    "phonnumber": phonnumber_r[0],
                                                                    'login_etebar':login_etebar[0],
                                                                    })
ignor_etebar = ['false']
melicod_ignor = ['']

def ignordef(request):
    ignor_etebar[0] = 'false'
    melicode = request.POST.get('melicode')
    button_send = request.POST.get('button_send')
    buttoncode_send = request.POST.get('buttoncode_send')
    inputcode_regester = request.POST.get('inputcode_regester')
    changhbutton = request.POST.get("changhbutton")
    newpass = request.POST.get("newpass")
    if (melicode != '') and (melicode != None) :
        melicod_ignor[0] = melicode
    if changhbutton == "accept":
        a = accuntmodel.objects.filter(melicode=melicod_ignor[0])
        a.update(pasword=newpass)
        e = 'succes'
        return render(request,'changepaswoord.html',context={'etebar': e})

    if (buttoncode_send != None) and (buttoncode_send != '') and (inputcode_regester != None) and (inputcode_regester != ''):
        users = accuntmodel.objects.all()
        for user in users:
            if user.melicode == melicod_ignor[0]:
                if inputcode_regester == user.pasword :
                    user_login = authenticate(request,
                                                 username=melicod_ignor[0],
                                                 password=inputcode_regester,
                                             )

                    if user_login is not None :
                        login (request,user_login)
                        return render(request,'changepaswoord.html')
                else:
                    e = 'false'
                    return render(request, 'code_cantact.html', context={'etebar': e}, )

    if button_send == 'accept':
        if (melicod_ignor[0] == '') or (melicod_ignor[0] == None) :
            ignor_etebar[0] = 'empty'
        if (melicod_ignor[0] != '') and (melicod_ignor[0] != None) :
            ignor_etebar[0] = 'nonempty'
            users = accuntmodel.objects.all()
            for user in users :
                if user.melicode == melicod_ignor[0] :
                    randomcode = random.randint(1000, 9999)
                    message = f"رمزجدید{randomcode}"
                    try:
                        api = KavenegarAPI(
                            '527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D')
                        params = {
                            'receptor': user.phonnumber,
                            'template': 'test',
                            'token': message,
                            'type': 'sms',
                        }
                        response = api.verify_lookup(params)
                        a = accuntmodel.objects.filter(melicode=user.melicode)
                        a.update(pasword=randomcode)
                        b = User.objects.filter(username=user.melicode)
                        b.delete()
                        User.objects.create_user(
                            username=melicod_ignor[0],
                            password=str(randomcode),
                            first_name=user.firstname,
                            last_name=user.lastname,
                        )

                        return render(request, 'code_cantact.html')
                    except APIException as e:
                        m = 'tellerror'
                        # messages.error(request,'در سیستم ارسال پیامک مشکلی پیش آمده لطفا شماره خود را به درستی وارد کنید و دوباره امتحان کنید در صورتی که مشکل برطرف نشد در اینستاگرام پیام دهید ')
                        return render(request, 'add_cantact.html',context={'melicod_etebar':m})
                    except HTTPException as e:
                        m = 'neterror'
                        # messages.error(request,'در سیستم ارسال پیامک مشکلی پیش آمده لطفا شماره خود را به درستی وارد کنید و دوباره امتحان کنید در صورتی که مشکل برطرف نشد در اینستاگرام پیام دهید ')
                        # return render(request, 'add_cantact.html')
                        return render(request, 'add_cantact.html', context={'melicod_etebar': m},)

    return render(request,'ignor_cantact.html',context={'ignor_etebar':ignor_etebar[0],})



def chengpaswoord(request):
    return render(request,'changepaswoord.html')