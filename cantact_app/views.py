from django.shortcuts import render , redirect
import tkinter
from tkinter import messagebox
import datetime
from jalali_date import date2jalali,datetime2jalali
from datetime import timedelta
from cantact_app.models import accuntmodel,savecodphon
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
year = [int(str('14' + stry(datetime.datetime.now())))]
year[0] =int(str('14' + stry(datetime.datetime.now())))
calandar_array_for_show = ['0']
calandar_array_for_show[0] ='0'
calandar_array_for_miladidate = [datetime.datetime.now()]
calandar_array_for_miladidate[0] = datetime.datetime.now()
calandar_array_for_shamsidate = [stradby(t[0])]
calandar_array_for_shamsidate [0] = stradby(t[0])
firstname_r = ['']
lastname_r = ['']
melicod_r = ['']
phonnumber_r = ['']
berthmiladi_r = [datetime.datetime.now()]
berthmiladi_r[0] = datetime.datetime.now()
melicod_etebar = ['true']
def addcantactdef(request):
    bbtn = request.POST.get("bbtn")
    input_year = request.POST.get("input_year")
    if (input_year == None) or (input_year == ''):
        input_year = str(year[0])
    button_upmounth = request.POST.get("button_upmounth")
    button_downmounth = request.POST.get("button_downmounth")
    button_calandar = request.POST.get("button_calandar")
    button_back = request.POST.get("button_back")
    button_send = request.POST.get('button_send')
    buttoncode_repeat = request.POST.get('buttoncode_repeat')
    buttoncode_send = request.POST.get('buttoncode_send')
    inputcode_regester = request.POST.get('inputcode_regester')
    formuser = accuntform(request.POST, request.FILES)
# ---------اگر دکمه تقئیم خورد سال رو به هم اکنون تغییر میده دقت شود که در مواد دیگه مثل بالا زدن-سال یا چیزی دیگه - button calandar برابر acceot میشد-----------------------------------متوجه شدم که placeholder-مقدارش داخل input خواهد بود----------------------------------------------------------------
    if button_calandar == "accept" :
        year[0] = int(str('14' + stry(datetime.datetime.now())))
        input_year = year[0]
        t[0] = datetime.datetime.now()
        calandar_array_for_show[0] = '0'
        calandar_array_for_miladidate[0] = datetime.datetime.now()
        calandar_array_for_shamsidate[0] = stradby(t[0])
        berthmiladi_r[0] = datetime.datetime.now()
    # ---------- در این قسمت داده هایی که به صفحه addcontact داده میشود در آرایه هایدمربوطه ذخیره میشه تا با زدن دکمه ها اونا نپرن ----
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
        # if len(str(melicod)) != 10:
        #     melicod_etebar[0] = 'repeat'
        #
        # try:
        #     melicod = str(int(melicod))
        # except:
        #     melicod_etebar[0] = 'stringerror'

        melicod_r[0] = melicod

    if melicod_r[0] == None :
        melicod_r[0] = ''

    phonnumber = request.POST.get("phonnumber")
    if (phonnumber != '') and ( phonnumber != None) :
        phonnumber_r[0] = phonnumber
    if phonnumber_r[0] == None :
        phonnumber_r[0] = ''
# ****************************************************کلید برگشت**********************************************
    if button_back == "accept" :
        melicod_r[0] = ''
        return redirect('/')
# -----------------------------------------------------------------انتخاب روز تولد----------------------------------------------
    if (bbtn != None) and (bbtn != '') and (calandar_array_for_show != None) and (calandar_array_for_show != '') :
        berthmiladi_r[0] = str(calandar_array_for_miladidate[int(bbtn)])
        return render(request,'add_cantact.html',context={ "firstname":firstname_r[0],
                                                           "lastname":lastname_r[0],
                                                           "melicod":melicod_r[0],
                                                           "phonnumber":phonnumber_r[0],
                                                           "year" : year[0],
                                                           "berthday_shamsi":calandar_array_for_shamsidate[int(bbtn)],
                                                           "melicod_etebar": 'true',
                                                           })
# ---------------------------------------------------------------------------------
    if(input_year != None) and (input_year != ''):
        if int(input_year) < 1200:
            input_year = 1402
        if int(input_year) > int(str('14' + stry(datetime.datetime.now()))):
            input_year = str(year[0])
        mounth_of_t = strb(t[0])
        while int(input_year) != year[0] :
            if int(input_year) < year[0] :
                if (strb(t[0]) == 'فروردین') and (strd(t[0]) == '1'):
                    year[0] -= 1
                    button_calandar = "accept"
                    button_upmounth = None
                    button_downmounth = None
                t[0] -= timedelta(days=1)
            if int(input_year) > year[0] :
                if (strb(t[0]) == 'فروردین') and (strd(t[0]) == '1'):
                    year[0] += 1
                    button_calandar = "accept"
                    button_upmounth = None
                    button_downmounth = None
                t[0] += timedelta(days=1)

        if strb(t[0]) == 'اسفند' :
            while strb(t[0]) != mounth_of_t :
                t[0] -= timedelta(days=1)
        if strb(t[0]) == 'فروردین' :
            while strb(t[0]) != mounth_of_t :
                t[0] += timedelta(days=1)
# ----------------------------------------------------------------------------------------------------------
    if button_upmounth == "accept" :
        button_calandar = "accept"
        mounth = strb(t[0])
        while strb(t[0]) == mounth :
            t[0] += timedelta(days=1)
        if strb(t[0]) == 'فروردین' :
            year[0] += 1
# -----------------------------------------------------------------------------------------------------
    if button_downmounth == "accept" :
        button_calandar = "accept"
        mounth = strb(t[0])
        while strb(t[0]) == mounth :
            t[0] -= timedelta(days=1)
        if strb(t[0]) == 'اسفند' :
            year[0] -= 1
# ------------------------------------------------------------------------------------------------------
    if button_calandar == "accept" :
        mounth = strb(t[0])
        day_of_mounth = strd(t[0])
        day_of_week = stra(t[0])
        r = 0
        g = 0
        calandar_array_for_show.clear()
        calandar_array_for_miladidate.clear()
        calandar_array_for_shamsidate.clear()

        for r in range(int(day_of_mounth)) :
            t[0] -= timedelta(days=1)
        while stra(t[0]) != 'جمعه' :
            t[0] -= timedelta(days=1)
            calandar_array_for_show.append('')
            calandar_array_for_miladidate.append(t[0])
            calandar_array_for_shamsidate.append(stradby(t[0]))

        calandar_array_for_show.append('')
        calandar_array_for_miladidate.append(t[0])
        calandar_array_for_shamsidate.append(stradby(t[0]))
        while strd(t[0]) != "1" :
            t[0] +=timedelta(days=1)
        i = 0
        while strb(t[0]) == mounth :
            i += 1
            calandar_array_for_show.append(i)
            calandar_array_for_miladidate.append(t[0])
            calandar_array_for_shamsidate.append(stradby(t[0]))
            t[0] += timedelta(days=1)
        t[0] -=timedelta(days=1)
        return render(request,'calander.html',context={"firstname":firstname_r[0],
                                                       "lastname":lastname_r[0],
                                                       "melicod":melicod_r[0],
                                                       "phonnumber":phonnumber_r[0],
                                                        "year" : year[0],
                                                        "mounth": mounth,
                                                        "calandar_aray":calandar_array_for_show,
                                                       })
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
            savecodphon.objects.create(firstname=firstname_r, lastname=lastname_r,melicode=str(melicod_r[0]),
                                       phonnumber=str(phonnumber_r[0]),berthday=str(berthmiladi_r[0]),code=str(randomcode),expaiercode="2",
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
            return render(request, 'add_cantact.html', context={"firstname": firstname_r[0],
                                                    "lastname": lastname_r[0],
                                                    "melicod": melicod_r[0],
                                                    "phonnumber": phonnumber_r[0],
                                                    "year": year[0],
                                                    # "berthday_shamsi": calandar_array_for_shamsidate[int(bbtn)],
                                                    "melicod_etebar": melicod_etebar[0],
                                                    })
# --------------------------------------------------------------------------------------------------------------------------------
    if (buttoncode_send != None) and (buttoncode_send != '') and (inputcode_regester != None) and (inputcode_regester != ''):
        savecods = savecodphon.objects.all()
        for savecode in savecods :
            if (int(savecode.code) == int(inputcode_regester)) and (int(savecode.melicode) == int(melicod_r[0])):
                    savecods = savecodphon.objects.all()
                    for savecode in savecods:
                        a = savecodphon.objects.filter(melicode=savecode.melicode)
                        a.delete()
                    accuntmodel.objects.create(
                        firstname=firstname_r[0],
                        lastname=lastname_r[0],
                        melicode=str(melicod_r[0]),
                        phonnumber=str( phonnumber_r[0]),
                        berthday=str(berthmiladi_r[0]),
                        pasword=str(phonnumber_r[0]),
                        )

                    User.objects.create_user(
                                                username=melicod_r[0],
                                                password=phonnumber_r[0],
                                                first_name=firstname_r[0],
                                                last_name=lastname_r[0],
                                            )

                    user_login =authenticate(request,
                                             username=melicod_r[0],
                                             password=phonnumber_r[0],
                                             )

                    login (request,user_login)
                    e = 'succes'
                    return render(request,'code_cantact.html',context={'etebar':e},)
                        # return redirect('/')
            # return render(request, 'cod_of_phon.html')
            else:
                e = 'false'
                return render(request, 'code_cantact.html', context={'etebar': e}, )



        # accuntmodel.objects.create(firstname=firstname_r[0],
        #                            lastname=lastname_r[0],
        #                            melicode=melicod_r[0],
        #                            phonnumber=phonnumber_r[0],
        #                            berthday=berthmiladi_r[0]
        #                            )
        # return redirect('/')

    return render(request,'add_cantact.html',context={'melicod_etebar':melicod_etebar[0]})
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
    return render(request,'login_cantact.html',context={'login_etebar':login_etebar[0],})
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