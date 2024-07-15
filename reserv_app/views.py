from django.shortcuts import render, redirect
from jobs_app.models import *
from cantact_app.models import accuntmodel
import datetime
from jalali_date import date2jalali,datetime2jalali
from datetime import timedelta
import matplotlib
from reserv_app.models import reservemodel,leavemodel,reservemodeltest,filepage1model,searchmodeltest
from cantact_app.models import accuntmodel
from file_app.models import fpeseshktestmodel
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

def reservdef(request):
    if request.user.is_authenticated:
# ---------اگر فردی که وارد شده است login  کرده باشد اینجا برایش در reservmodeltest  یک object ساخته میشود-----------
        melicodcheck = "false"
        rtotal = reservemodeltest.objects.all()
        for r in rtotal :
            if r.mellicode == request.user.username:
                melicodcheck = "true"

        if melicodcheck == "false" :
            reservemodeltest.objects.create(
                mellicode= request.user.username
            )
# ----------با توجه به کد ملی فرد login شده اسم کوچک و بزرگ او را پیدا میکنیم---------------------------
        users = accuntmodel.objects.all()
        for user in users:
            if user.melicode == request.user.username:
                level[0] = user.level
                ferstname_user = user.firstname
                lastname_user = user.lastname
                mellicoduser[0] = user.melicode
                # us = reservemodeltest.objects.all()
                # for u in us:
                #     if u.mellicode == request.user.username:
                #         bb = reservemodeltest.objects.filter(mellicode=request.user.username)
                #         bb.delete()

                a = reservemodeltest.objects.filter(mellicode=request.user.username)
                a.update(fiestname=user.firstname, lastname=user.lastname , phonnumber=user.phonnumber)
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
#**********************انتخاب کاربر به صورت یک عدد از forloop  از وب میاد و در اینجا اون عدد تبدیل میشه به انتخاب اصلی و در  f  ریخته میشه**************
        c = 0
        if inputwork != None:
            reservposition[0] = "1"
            for f in works :
                if int(c) == int(inputwork) :
                    selectprocedure.clear()
                    selectprocedure.append(f.work)
                    selectprocedure.append(f.detalework)
                    selectprocedure.append(f.person)
                    a = reservemodeltest.objects.filter(mellicode=request.user.username)
                    a.update(jobreserv=f.work,
                             detalereserv=f.detalework,
                             personreserv=f.person,
                             vahed=f.vahed,
                             )

                    if f.time == "زمان کمی میبرد" :
                        sel = "0"
                        selectprocedure.append("0")
                    if f.time == "نیم ساعت" :
                        sel = "1"
                        selectprocedure.append("1")
                    if f.time == "یک ساعت" :
                        sel = "2"
                        selectprocedure.append("2")
                    if f.time =="یک و نیم ساعت" :
                        sel = "3"
                        selectprocedure.append("3")
                    if f.time == "دو ساعت" :
                        sel = "4"
                        selectprocedure.append("4")
                    if f.time == "دو نیم ساعت" :
                        sel = "5"
                        selectprocedure.append("5")
                    selectprocedure.append(f.cast)
                    a = reservemodeltest.objects.filter(mellicode=request.user.username)
                    a.update(
                             timereserv=sel,
                             castreserv=f.cast,
                             )

                c +=1

            shamsiarray.clear()
            miladiarray.clear()
            day.clear()
            res = reservemodel.objects.all()
            reservmovaghats = reservemodeltest.objects.all()
            # ___________در این قسمت تعداد روزهایی که قرار هستش به مراجعه کننده نشون بدیم مشخص میشه____
            tedaderooz = 10
            # __________آرایه shmsiarray_ساخته میشه به تعداد tedaderooz  به ترتیب از امروز روز میچینه تو خودش________
            t = datetime.datetime.now()
            for i in range(tedaderooz) :
                shamsiarray.append(stradb(t))
                miladiarray.append(t.strftime('%a %d %b %y'))

# ____________در آرایه ی dayarr  بیست تا true مسازه که برای هر روز نشانه ازاد بودن بیست تایم ده صبح تا 8 شب هستش________
# _________بعد میاد محدودیتها رو اعمال میکنه و هذ تایم رو براساس محدودتها ممکنه false کنه یا true نگه داره_________
                dayarr = ['t']
                dayarr.clear()
                dayarr.append(stradb(t))
                for h in range(20):
                    dayarr.append('true')
# _____برسی مرخصی ها و حضور اپراتوری که انتخاب شده_________
                day_leave = strd(t)
                ls = leavemodel.objects.all()
                users = accuntmodel.objects.all()
                for user in users:
                    if user.firstname + ' ' + user.lastname == selectprocedure[2] :
                        for l in ls :
                            if (l.personelmelicod == user.melicode) and (l.muont == strb(t)) :
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
        # -------------------------اینجا رزرو های قبلی رو چک میکنه---------
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
# # ---------------------------------------------اگر کاری مه انتخاب شده بیش از نیم ساعت باشه یعنی دو تا نیم ساغت یا سه  یا پهارتا یا پنج تا نیم ساعت باشه-----------
# # ------باید چک شود که تا تایم های اینده اش  به همون اندازه که وقت میخواد وقت باشه ---------------------------------------
#
                if selectprocedure[3] == "2" :
                    for hh in range(19) :
                        hh += 1
                        if dayarr[int(hh) + 1] == "false" :
                            dayarr[int(hh)] = "false"
                    dayarr[20] = "false"
                if selectprocedure[3] == "3" :
                    for hh in range(18) :
                        hh += 1
                        if dayarr[int(hh) + 1] == "false" :
                            dayarr[int(hh)] = "false"
                        if dayarr[int(hh) + 2] == "false":
                            dayarr[int(hh)] = "false"
                    dayarr[19] = "false"
                    dayarr[20] = "false"
                if selectprocedure[3] == "4" :
                    for hh in range(17) :
                        hh += 1
                        if dayarr[int(hh) + 1] == "false" :
                            dayarr[int(hh)] = "false"
                        if dayarr[int(hh) + 2] == "false":
                            dayarr[int(hh)] = "false"
                        if dayarr[int(hh) + 3] == "false":
                            dayarr[int(hh)] = "false"
                    dayarr[18] = "false"
                    dayarr[19] = "false"
                    dayarr[20] = "false"
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
                    dayarr[17] = "false"
                    dayarr[18] = "false"
                    dayarr[19] = "false"
                    dayarr[20] = "false"
#
                t += timedelta(days=1)
                day.append(dayarr)
# --------------------------اگر ابن دوخظ انجام شه دو دیتای اول در ارایه ی روزها پاک خواهد شد یعنی ار دو روز بعد میتونن نوبا بگیرن--------------
# -----ولی اگه بخوایم این کار رو بکنیم باید ارایه های شمسی و میلادی هم از دوتا دور تر خونده بشن یغنی یغنی خط.ط 301 و 302 عوض شنبه جای اینکه از اول خوانده بشن از دوتا جلوتر خوانده بشن
            # day.pop(0)
            # day.pop(0)
            return render(request,'timereserv.html',context={
                                                             'day':day,
                                                             'person':" رزرو وقت برای " + selectprocedure[0] +" "+ selectprocedure[1] + "(" + selectprocedure[2] + ")",
                                                             })
# _______انتخاب یه تایم برای خدمت مورد نظر__________
        if (timeselect != None) and (timeselect != '') :
            # reservposition[0] = 2
            s = timeselect
            stime = s.split(",")
            ttime = datetime.datetime.now()
            for tt in range(int(stime[1])) :
                ttime += timedelta(days=1)
            ttime -= timedelta(days=1)
            a = reservemodeltest.objects.filter(mellicode=request.user.username)
            a.update(
                dateshamsireserv=stradb(ttime),
                datemiladireserv=ttime.strftime('%a %d %b %y'),
                yearshamsi=stry(datetime.datetime.now()),
                numbertime=stime[0],
            )
            selectprocedure.append(stradb(ttime))
            selectprocedure.append(ttime.strftime('%a %d %b %y'))
            selectprocedure.append(stry(datetime.datetime.now()))
            selectprocedure.append(stime[0])
            s = ""
            if stime[0] == "1"  :
                s ="10"
                selectprocedure.append("10")
            if stime[0] == "2"  :
                s ="10.5"
                selectprocedure.append("10.5")
            if stime[0] == "3"  :
                s ="11"
                selectprocedure.append("11")
            if stime[0] == "4"  :
                s ="11.5"
                selectprocedure.append("11.5")
            if stime[0] == "5"  :
                s ="12"
                selectprocedure.append("12")
            if stime[0] == "6"  :
                s ="12.5"
                selectprocedure.append("12.5")
            if stime[0] == "7"  :
                s ="13"
                selectprocedure.append("13")
            if stime[0] == "8"  :
                s ="13.5"
                selectprocedure.append("13.5")
            if stime[0] == "9"  :
                s ="14"
                selectprocedure.append("14")
            if stime[0] == "10"  :
                s ="14.5"
                selectprocedure.append("14.5")
            if stime[0] == "11"  :
                s ="15"
                selectprocedure.append("15")
            if stime[0] == "12"  :
                s ="15.5"
                selectprocedure.append("15.5")
            if stime[0] == "13"  :
                s ="16"
                selectprocedure.append("16")
            if stime[0] == "14"  :
                s ="16.5"
                selectprocedure.append("16.5")
            if stime[0] == "15"  :
                s ="17"
                selectprocedure.append("17")
            if stime[0] == "16"  :
                s ="17.5"
                selectprocedure.append("17.5")
            if stime[0] == "17"  :
                s ="18"
                selectprocedure.append("18")
            if stime[0] == "18"  :
                s ="18.5"
                selectprocedure.append("18.5")
            if stime[0] == "19"  :
                s ="19"
                selectprocedure.append("19")
            if stime[0] == "20"  :
                s ="19.5"
                selectprocedure.append("19.5")
            a = reservemodeltest.objects.filter(mellicode=request.user.username)
            a.update(hourreserv=s)
            reservs = reservemodel.objects.all()
            reservetebar[0] = 'succes'
            filepage1 = "false"
            page =filepage1model.objects.all()
            for p in page :
                if p.mellicode == request.user.username :
                    filepage1 = "true"
            if filepage1 == "false" :
                return render(request,'add_userfilebotax.html')
            else:
                rtotal = reservemodeltest.objects.all()
                for r in rtotal:
                    if r.mellicode == request.user.username:
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
            rtotal = reservemodeltest.objects.all()
            for r in rtotal:
                if r.mellicode == request.user.username:
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
                                                                        })
        return render(request,'reserv.html',context={'works':works,
                                                 'job':ww,
                                                 'shamsiarray':shamsiarray,
                                                 })
    else:
        loginetebar[0] = "false"
        return render(request,'home.html',context={"loginetebar":loginetebar[0]})

# _________________________اینجا کارمندان تایمهایی که قرار هست نیان سر کار رو مشخص میکن و در leavemodel.leave_ ذخیره میکنن_____________
leaveshamsi = ['0']
leavemiladi = ['0']
leavearray = ['0']
def leave(request):
    timeleave = request.POST.get("timeleave")

    # ***************با زدن هر تاریخ اون به فایل مرخصی**************
    if (timeleave != None) and (timeleave != ''):
        leavepersonals = leavemodel.objects.all()
        e = 0
#*************************************************اگر e=0 باشه  یعنی تا به حال این فرد تایم کاری نداده یا برای این ماه نداده و پس میره پایین براش یه object ساخته میشه*****
# ******************************اگر قبلا تایم داده یا در حال تایم دادن هستش دو تا اتفاق ممکنه اینکه بخواد تایم داده شده رو حذف کنه یا تایم جدید بده**
# *****اول چک میشه که اون تایمی که انتخاب شده آیا در لیست تایم های ثبت شده در leave هستش   یا نه اگر بود میره اونو حذف میکنه و leave جدید میسازه*******
        for personel in leavepersonals:
            if (personel.personelmelicod == request.user.username) and (personel.muont == strb(datetime.datetime.now())):
                e = 1
         # ________________شروع چک برای اینکه ببینه تکراریه یا نه_____اگه تکراری باشه e =2 میشه____________________
                leave = personel.leave

                s = personel.leave.split(",")
                s_inter = timeleave.split(",")
                d_save = ['t']
                d_save.clear()
                a = 2
                for i in range(int(len(s))) :
                    if a <= len(s) :
                        d_save.append(s[int(a)])
                        a +=2
                for i in range(int(len(d_save))) :
                    if s_inter[1] == d_save[i] :
                        if s_inter[0] == s[((i*2)+1)] :
                            s.pop(((i*2)+1))
                            s.pop(((i*2)+1))
                            d = "0"
                            for i in s :
                                if i != "0":
                                    d = d +","+ i
                            l = leavemodel.objects.filter(personelmelicod=request.user.username)
                            l.update(leave=d)
                            e = 2
                            break
        # _____________اگه e=2 نباشه یعنی اون تایم انتخاب شده جدید هست و باید به leave قبلی اضافه بشه_____________
                if e == 1 :
                    a = 2
                    for i in range(int(len(s))):
                        if a <= len(s):
                            if (int(s[a]) ==s_inter[1]) and (int(s[a-1]) == s_inter[0]):
                                leavearray[int(s[a]) - 1][int(s[a - 1])] = "false"
                            a += 2
                        else:
                            break

                    leave = leave + ',' + timeleave
                    l = leavemodel.objects.filter(personelmelicod=request.user.username)
                    l.update(leave=leave)
        # ________________اگر e=2 و e=1 نباشه و همون صفر باقی مانده باشه یعنی ماه جدیده یا فرد جدیده___________
        if e == 0:
            leavemodel.objects.create(personelmelicod=str(request.user.username),
                                      dateshamsi=stradby(datetime.datetime.now()),
                                      datemiladi=datetime.datetime.now().strftime('%a %d %b %y'),
                                      muont = strb(datetime.datetime.now()),
                                      leave='0' + ',' + timeleave)

        s = timeleave
        stime = s.split(",")

    # ***********ماه رو میسازه و یه آرایه درست میکنه شامل روز و بیست تاtrue ***********
    t = datetime.datetime.now()
    m = strb(t)
    leavearray.clear()
    for i in range(31) :
        if m != strb(t) :
            break
        t -= timedelta(days=1)

    t += timedelta(days=1)
    for i in range(31):
        dayleave = ['t']
        dayleave.clear()
        dayleave.append(stradb(t))
        for h in range(20):
            dayleave.append('true')
        leavearray.append(dayleave)
        t += timedelta(days=1)
        if m != strb(t) :
            break
# **************************************************************************************
    leavepersonals = leavemodel.objects.all()
    s = ""
    for personel in leavepersonals :
        if (personel.personelmelicod == request.user.username) and (personel.muont == strb(datetime.datetime.now())):
            s = personel.leave.split(",")
    a = 2
    for i in range(int(len(s))) :
        if a <= len(s):
            leavearray[int(s[a]) - 1][int(s[a - 1])] = "false"
            a += 2
        else:
            break
    return render(request,'leave.html',context={"leavearray":leavearray,})

def reserverdef(request):
    dayreserv = ['t']
    dayreserv.clear()
    t = datetime.datetime.now()
    dayarr = ['t']
    dayarr.clear()
    dayarr.append(stradb(t))
    for h in range(20):
        dayarr.append('')
    rs = reservemodel.objects.all()
    for r in rs:
        if r.datemiladireserv == t.strftime('%a %d %b %y') :
            us = accuntmodel.objects.all()
            for u in us:
                if r.melicod == u.melicode :
                    name = u.firstname + " " + u.lastname
            dayarr[int(r.numbertime)] = name + " " + r.jobreserv + " " + r.detalereserv + " " + r.personreserv + " " + "بیعانه:" + " " + r.pyment
            i = 1
            while i < int(r.timereserv):
                dayarr[int(r.numbertime)+i] = "false"
                i += 1

    dayreserv.append(dayarr)

    return render(request,'reserver.html', context={
        'day': dayreserv,
    })

def dashborddef(request):
    users = accuntmodel.objects.all()
    namedashbord = ''
    for user in users:
        if user.melicode == request.user.username:
            namedashbord = user.firstname + ' ' + user.lastname

    dayreserv = ['t']
    dayreserv.clear()


    t = datetime.datetime.now()
    dayconterstr = request.POST.get("dayconter")
    if (dayconterstr == None) or (dayconterstr == ""):
        dayconter = 0
    else:
        dayconter = int(dayconterstr)
    button_next = request.POST.get("button_next")
    if button_next == 'accept' :
        dayconter += 1
    button_back = request.POST.get("button_back")
    if button_back == 'accept' :
        dayconter -= 1
    if dayconter < 0 :
        dayconterm = dayconter * (-1)
        for i in range(dayconterm):
            t -= timedelta(days=1)
    if dayconter > 0 :
        for i in range(dayconter):
            t += timedelta(days=1)


    dayarr = ['t']
    dayarr.clear()
    dayarr.append(stradb(t))
    for h in range(21):
        dayarr.append('')
    rs = reservemodel.objects.all()
    name = ''
    for r in rs:
        if (r.datemiladireserv == t.strftime('%a %d %b %y')) and (r.personreserv == namedashbord ) and (r.checking != 'true') :
            us = accuntmodel.objects.all()
            for u in us:
                if r.melicod == u.melicode :
                    name = u.firstname + " " + u.lastname
            dayarr[int(r.numbertime)] = name + " " + r.jobreserv + " " + r.detalereserv + " " + r.personreserv + " " + "بیعانه:" + " " + r.pyment
            i = 1
            while i < int(r.timereserv):
                dayarr[int(r.numbertime)+i] = "false"
                i += 1
    dayreserv.append(dayarr)

    dastiarray = ['']
    dastiarray.clear()
    rs = reservemodel.objects.all()
    for r in rs:
        if (r.datemiladireserv == t.strftime('%a %d %b %y')) and (r.personreserv == namedashbord ) and (r.numbertime == "21"):
            us = accuntmodel.objects.all()
            for u in us:
                if r.melicod == u.melicode :
                    name = u.firstname + " " + u.lastname
            dastiarray.append([(name + " " + r.jobreserv + " " + r.detalereserv + " " + r.personreserv + " " + "بیعانه:" + " " + r.pyment),str(r.id)])



    timeselect = request.POST.get('timeselect')
    if ( timeselect != None ) and ( timeselect != '' ):
        se = timeselect.split(",")
        tt = int(se[1])
        time = datetime.datetime.now()
        # while tt != 1 :
        #     if tt < 1 :
        #         time -= datetime.timedelta(days=1)
        #         tt += 1
        #     if tt > 1:
        #         time += datetime.timedelta(days=1)
        #         tt -= 1
        reservs = reservemodel.objects.all()
        reservselectid = 0
        n = ''
        for reserv in reservs:
            if str(int(se[0])) == "21":
                if str(reserv.id) == str(int(se[1])):
                    n = ''
                    qs = accuntmodel.objects.all()
                    for q in qs:
                        if q.melicode == reserv.melicod:
                            n = q.firstname + " " + q.lastname
                    return render(request,'f1_pezeshk.html',context={
                        'name':n,
                        'procedure':reserv.jobreserv + " " + reserv.detalereserv,
                        'id':reserv.id,
                        'vahed':reserv.vahed,
                                                                            })
            else:
                if (reserv.personreserv == namedashbord) and (reserv.datemiladireserv == time.strftime('%a %d %b %y')) and ( int(se[0]) == int(reserv.numbertime)) :
                    n = ''
                    qs = accuntmodel.objects.all()
                    for q in qs:
                        if q.melicode == reserv.melicod:
                            n = q.firstname + " " + q.lastname

                    return render(request,'f1_pezeshk.html',context={
                        'name':n,
                        'procedure':reserv.jobreserv + " " + reserv.detalereserv,
                        'id':reserv.id,
                        'vahed':reserv.vahed,
                                                                                })
    reservid = request.POST.get("reservid")
    fpezeshkibottom = request.POST.get("fpezeshkibottom")
    vahedeobject = request.POST.get("vahedeobject")
    vahedeobjectname = request.POST.get("vahedeobjectname")
    cast = ''
    if fpezeshkibottom == "accept" :
        ws = reservemodel.objects.all()
        for w in ws:
            cast = w.castreserv
            if int(w.id) == int(reservid) :
                if (vahedeobject != None) and (vahedeobject != ''):
                    cast = str(float(w.castreserv) * float(vahedeobject))
                else:
                    vahedeobject = '1'

                fpeseshktestmodel.objects.create(
                    melicod=w.melicod,
                    jobreserv =w.jobreserv,
                    detalereserv =w.detalereserv,
                    personreserv =w.personreserv,
                    timereserv =w.timereserv,
                    castreserv =cast,
                    numbertime =w.numbertime,
                    hourreserv =w.hourreserv,
                    dateshamsireserv =w.dateshamsireserv,
                    datemiladireserv =w.datemiladireserv,
                    yearshamsi =w.yearshamsi,
                    cardnumber =w.cardnumber,
                    pyment =w.pyment,
                    trakingcod =w.trakingcod,
                    bank =w.bank,
                    checking =w.checking,
                    vahedeobject = vahedeobject,
                    vahedeobjectname = w.vahed,
                    reservid = reservid,
                )
                a = reservemodel.objects.filter(id=int(reservid))
                a.delete()
                return redirect('/')

    return render(request,'dashbord.html',context={
                                                                'dastiarray':dastiarray,
                                                                'day': dayreserv,
                                                                'dayconter':dayconter,
                                                                })
def reservdasti(request):
    job = request.POST.get("job")
    melicode = request.POST.get("melicode")
    detalework = request.POST.get("detalework")
    button_send = request.POST.get("button_send")
    castreserv = request.POST.get("castreserv")
    personreserv = request.POST.get("personreserv")
    namebuttom = request.POST.get('namebuttom')
    names =request.POST.get("names")
    tickon = request.POST.get("tickon")

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
            'arrayname':arrayname
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


    js = jobsmodel.objects.all()
    jobarray = ['']
    jobarray.clear()
    for j in js:
        s = (j.job+","+str(j.id)).split(",")
        jobarray.append(s)

    detalarray = ['']
    detalarray.clear()
    if ( job != None ) and ( job != ''):
        ws = workmodel.objects.all()
        for w in ws:
            if w.idjob == job :
                p = (w.detalework+","+str(w.id)).split(",")
                detalarray.append(p)


    ws = workmodel.objects.all()
    timereserv = "0"
    vahed = ''
    d = '0'
    for w in ws:
        if str(w.id) == str(detalework):
            personreserv = w.person
            castreserv =w.cast
            d = w.detalework
            vahed = w.vahed
    jj = '0'
    jes = jobsmodel.objects.all()
    for je in jes:
        if str(je.id) == str(job):
            jj = je.job
    numbertime = '21'
    hourreserv = 'timeout'
    dateshamsireserv = stradby(datetime.datetime.now())
    datemiladireserv = datetime.datetime.now().strftime('%a %d %b %y')
    yearshamsi = stry(datetime.datetime.now())
    etebarreservdasti = 'notr'
    if button_send == 'accept':
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
            pyment = "0",
            vahed=vahed,
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

    })



