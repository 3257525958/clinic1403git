from django.shortcuts import render, redirect
from jobs_app.models import workmodel
from cantact_app.models import accuntmodel
import datetime
from jalali_date import date2jalali,datetime2jalali
from datetime import timedelta
import matplotlib
from reserv_app.models import reservemodel,leavemodel,reservemodeltest,neursetestmodel
from cantact_app.models import accuntmodel
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
def reservdef(request):
    if request.user.is_authenticated:
        users = accuntmodel.objects.all()
        for user in users:
            if user.melicode == request.user.username:
                level[0] = user.level
                ferstname_user = user.firstname
                lastname_user = user.lastname
                mellicoduser[0] = user.melicode
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
                    print(selectprocedure)
                    selectprocedure.append(f.work)
                    selectprocedure.append(f.detalework)
                    selectprocedure.append(f.person)

                    if f.time == "نیم ساعت" :
                        selectprocedure.append("1")
                    if f.time == "یک ساعت" :
                        selectprocedure.append("2")
                    if f.time =="یک و نیم ساعت" :
                        selectprocedure.append("3")
                    if f.time == "دو ساعت" :
                        selectprocedure.append("4")
                    if f.time == "دو نیم ساعت" :
                        selectprocedure.append("5")
                    selectprocedure.append(f.cast)
                c +=1

            shamsiarray.clear()
            miladiarray.clear()
            day.clear()
            reservs = reservemodel.objects.all()
            # ___________در این قسمت تعداد روزهایی که قرار هستش به مراجعه کننده نشون بدیم مشخص میشه____
            t = datetime.datetime.now()
            mount = strb(t)
            tedaderooz = 0
            # _________اگه از روز بیستم ماه گذشته باشه30 روز نمایش داده میشه_________
            if int(strd(t)) <= 20 :
                for i in range(30) :
                    if strb(t) != mount :
                        break
                    tedaderooz += 1
                    t += timedelta(days=1)
            t = datetime.datetime.now()
            # _________و اگه قبل از بیستم ماه باشه فقط تا اخر ماه تعداد روز های قابل مشاهده خواهند بود_______
            if int(strd(t)) > 20 :
                tedaderooz = 30
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
                                for i in range(int(len(s))):
                                    if a <= len(s):
                                        if s[a] == strd(t):
                                            dayarr[int(s[a-1])] = "false"

                                        a += 2
                                    else:
                                        break

                for r in reservs :
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
                if selectprocedure[3] == "2" :
                    for hh in range(19) :
                        if dayarr[int(hh) + 1] == "false" :
                            dayarr[int(hh)] = "false"
                    dayarr[20] = "false"
                if selectprocedure[3] == "3" :
                    for hh in range(18) :
                        if dayarr[int(hh) + 1] == "false" :
                            dayarr[int(hh)] = "false"
                        if dayarr[int(hh) + 2] == "false":
                            dayarr[int(hh)] = "false"
                    dayarr[19] = "false"
                    dayarr[20] = "false"
                if selectprocedure[3] == "4" :
                    for hh in range(17) :
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

                t += timedelta(days=1)
                day.append(dayarr)
            day.pop(0)
            day.pop(0)

            return render(request,'timereserv.html',context={'day':day,
                                                             'person':" رزرو وقت برای " + selectprocedure[0] +" "+ selectprocedure[1] + "(" + selectprocedure[2] + ")",
                                                             })
# _______انتخاب یه تایم برای خدمت مورد نظر__________
        if (timeselect != None) and (timeselect != '') :
            reservposition[0] = 2
            s = timeselect
            stime = s.split(",")
            selectprocedure.append(shamsiarray[int(stime[1])+1])
            selectprocedure.append(miladiarray[int(stime[1])+1])
            selectprocedure.append(stry(datetime.datetime.now()))
            selectprocedure.append(stime[0])
            if stime[0] == "1"  :
                selectprocedure.append("10")
            if stime[0] == "2"  :
                selectprocedure.append("10.5")
            if stime[0] == "3"  :
                selectprocedure.append("11")
            if stime[0] == "4"  :
                selectprocedure.append("11.5")
            if stime[0] == "5"  :
                selectprocedure.append("12")
            if stime[0] == "6"  :
                selectprocedure.append("12.5")
            if stime[0] == "7"  :
                selectprocedure.append("13")
            if stime[0] == "8"  :
                selectprocedure.append("13.5")
            if stime[0] == "9"  :
                selectprocedure.append("14")
            if stime[0] == "10"  :
                selectprocedure.append("14.5")
            if stime[0] == "11"  :
                selectprocedure.append("15")
            if stime[0] == "12"  :
                selectprocedure.append("15.5")
            if stime[0] == "13"  :
                selectprocedure.append("16")
            if stime[0] == "14"  :
                selectprocedure.append("16.5")
            if stime[0] == "15"  :
                selectprocedure.append("17")
            if stime[0] == "16"  :
                selectprocedure.append("17.5")
            if stime[0] == "17"  :
                selectprocedure.append("18")
            if stime[0] == "18"  :
                selectprocedure.append("18.5")
            if stime[0] == "19"  :
                selectprocedure.append("19")
            if stime[0] == "20"  :
                selectprocedure.append("19.5")
            reservs = reservemodel.objects.all()
            reservetebar[0] = 'succes'
            if selectprocedure[3] == "1" :
                reservetebar[0] = "succes"
            t = 0
            if selectprocedure[3] == '2' :
                t = int(selectprocedure[8])
                for r in reservs :
                    if r.personreserv == selectprocedure[2] :
                        if r.dateshamsireserv == selectprocedure[5] :
                            if int(r.timereserv) == int(t) +1:
                                reservetebar[0] = "false2"
            if selectprocedure[3] == '3' :
                t = int(selectprocedure[8])
                for r in reservs :
                    if r.personreserv == selectprocedure[2] :
                        if r.dateshamsireserv == selectprocedure[5] :
                            if int(r.timereserv) == int(t) +1:
                                reservetebar[0] = "fals3"
                            if int(r.timereserv) == int(t) + 2:
                                reservetebar[0] = "false3"
            if selectprocedure[3] == '4' :
                t = int(selectprocedure[8])
                for r in reservs :
                    if r.personreserv == selectprocedure[2] :
                        if r.dateshamsireserv == selectprocedure[5] :
                            if int(r.timereserv) == int(t) + 1:
                                reservetebar[0] = "false4"
                            if int(r.timereserv) == int(t) + 2:
                                reservetebar[0] = "false4"
                            if int(r.timereserv) == int(t) + 3:
                                reservetebar[0] = "false4"
            if selectprocedure[3] == '5' :
                t = int(selectprocedure[8])
                for r in reservs :
                    if r.personreserv == selectprocedure[2] :
                        if r.dateshamsireserv == selectprocedure[5] :
                            if int(r.timereserv) == int(t) + 1:
                                reservetebar[0] = "false5"
                            if int(r.timereserv) == int(t) + 2:
                                reservetebar[0] = "false5"
                            if int(r.timereserv) == int(t) + 3:
                                reservetebar[0] = "false5"
                            if int(r.timereserv) == int(t) + 4:
                                reservetebar[0] = "false5"
            if reservetebar[0] == 'succes' :
                reservemodeltest.objects.create(jobreserv=selectprocedure[0],
                                            detalereserv=selectprocedure[1],
                                            personreserv=selectprocedure[2],
                                            timereserv=selectprocedure[3],
                                            castreserv=selectprocedure[4],
                                            dateshamsireserv=selectprocedure[5],
                                            datemiladireserv=selectprocedure[6],
                                            yearshamsi=selectprocedure[7],
                                            numbertime=selectprocedure[8],
                                            hourreserv=selectprocedure[9],
                                            mellicode= mellicoduser[0]
                                            )
                return render(request,'add_userfilebotax.html')
            else:
                return render(request,'timereserv.html',context={'reservetebar':reservetebar[0],})
# ___________________تشکیل پرونده___________
        if filesendbutton == "accept" :
            reservposition[0] = "3"
            if (inject_botax == "yes") or (inject_botax == "no") :
                file_botax[0] = inject_botax
            else:
                error = "inject_botax"
                return render(request, 'add_userfilebotax.html', context={"error": error})
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
            neursetestmodel.objects.create(
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
            return render(request,'reserv_end.html',context={"selectprocedure":selectprocedure,
                                                             "firstname":ferstname_user,
                                                             "lastname":lastname_user,})
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