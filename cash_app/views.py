from cash_app.models import castmodel
from django.contrib.auth import authenticate, login
from django.shortcuts import render , redirect
from django.views import View
import requests
from django.conf import settings
import requests
import json
from django.http import HttpResponse, HttpRequest
from kavenegar import KavenegarAPI, APIException, HTTPException
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
import datetime
from datetime import timedelta
from jalali_date import date2jalali,datetime2jalali
from cantact_app.views import strb,stry,strd
from reserv_app.models import *
from jobs_app.models import jobsmodel,employeemodel,workmodel
from cash_app.models import *
from cantact_app.models import accuntmodel
from cantact_app.views import *
from file_app.models import *
from accountancy_app.models import *

ZIB_API_REQUEST = "https://gateway.zibal.ir/v1/request"
ZIB_API_VERIFY = "https://gateway.zibal.ir/verify"
ZIB_API_STARTPAY = "https://gateway.zibal.ir/start/"
ZIB_API_TOKEN = 'https://gateway.zibal.ir/v1/verify'

# CALLBACK_ZIBAL_URL = 'http://127.0.0.1:8000/zib/verifyzibal/'
MERCHANT_ZIBAL = 'zibal'
# ENDURL = "http://127.0.0.1:8000"

ENDURL = "https://drmahdiasadpour.ir"
CALLBACK_ZIBAL_URL = 'https://drmahdiasadpour.ir/zib/verifyzibal/'
# MERCHANT_ZIBAL = '64c2047fcbbc270017f4c6b2'

def orderzibal(request):
    if request.user.is_authenticated:
        request.session['melicode'] = request.user.username
        print(request.user.username)
        # ۱. بارگذاری اطلاعات رزرو و محاسبه مبلغ و موبایل
        work = workmodel.objects.all()
        for w in work:
            if w.id == int(request.session.get('selected_option_id')):
                peyment     = int(w.cast) // 5
                phonnumber  = str(w)
        users = accuntmodel.objects.all()
        for u in users:
            if int(u.melicode) == int(request.session.get('national_code')):
                phonnumber  = str(u.phonnumber)

        # ۲. آماده‌سازی payload برای درگاه
        payload = {
            "merchant":    MERCHANT_ZIBAL,
            "amount":      peyment,
            "callbackUrl": CALLBACK_ZIBAL_URL,
            "description": "بیعانه جهت رزرو",
            "orderId":     "ZBL",
            "mobile":      phonnumber
        }
        headers = {
            'Content-Type':   'application/json',
            'Content-Length': str(len(json.dumps(payload)))
        }

        # ۳. ارسال درخواست به درگاه با timeout
        try:
            response = requests.post(
                ZIB_API_REQUEST,
                json=payload,
                headers=headers,
                timeout=30
            )
        except requests.RequestException as e:
            # هر خطای شبکه‌ای یا timeout را با 502 برمی‌گردانیم
            return HttpResponse(f"خطا در ارتباط با سرویس پرداخت: {e}", status=502)

        # ۴. پردازش پاسخ درگاه
        if response.status_code == 200:
            result = response.json()
            if result.get('result') == 100:
                # موفق: ذخیره کد رهگیری و ریدایرکت به صفحه پرداخت 2
                reservemodeltest.objects.filter(
                    mellicode=request.user.username
                ).update(rahgiricod=str(result['trackId']))
                return redirect(f"{ZIB_API_STARTPAY}{result['trackId']}")
            else:
                # نتیجه ناموفق ولی پاسخ از سرور آمده است
                error_msg = result.get('message', 'خطای نامشخص در پرداخت')
                return HttpResponse(f"پرداخت انجام نشد: {error_msg}", status=400)
        else:
            # هر کد وضعیت غیر 200 از درگاه را پاس می‌دهیم
            return HttpResponse(
                f"خطای سرور درگاه ({response.status_code})",
                status=response.status_code
            )
    else:
        return redirect('/cantact/login/')

def callbackzibal(request):
    backbutton = request.GET.get('backbutton')
    if (backbutton != "") and (backbutton != None) :
        ur = f"{ENDURL}/?r={backbutton}"
        # ur = ENDURL
        return redirect(ur)

    trac = request.GET['trackId']
    data = {
        "merchant": MERCHANT_ZIBAL,
        "trackId": trac
    }
    data = json.dumps(data)
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    res = requests.post(ZIB_API_VERIFY, data=data, headers=headers)
    if res.status_code == 200:
        r = res.json()
        if r['message'] == 'success':
            a = reservemodeltest.objects.filter(rahgiricod=trac)
            a.update(message='success',
                     cardnumber=str(r['cardNumber']),
                    )
            allreserv = reservemodeltest.objects.all()
            for oneobj in allreserv:
                if oneobj.rahgiricod == trac :
                    firstname = oneobj.fiestname
                    lastname = oneobj.lastname
                    rahgiricode = oneobj.rahgiricod
                    kolkhedmat = oneobj.jobreserv+" "+oneobj.detalereserv+" توسط "+oneobj.personreserv
                    day = oneobj.dateshamsireserv
                    houre = oneobj.hourreserv

                    reservemodel.objects.create(
                                                        melicod =oneobj.mellicode,
                                                        jobreserv=oneobj.jobreserv,
                                                        detalereserv=oneobj.detalereserv,
                                                        personreserv=oneobj.personreserv,
                                                        timereserv=oneobj.timereserv,
                                                        castreserv=oneobj.castreserv,
                                                        numbertime=oneobj.numbertime,
                                                        hourreserv=oneobj.hourreserv,
                                                        dateshamsireserv=oneobj.dateshamsireserv,
                                                        datemiladireserv=oneobj.datemiladireserv,
                                                        yearshamsi=oneobj.yearshamsi,
                                                        cardnumber=oneobj.cardnumber,
                                                        pyment=str(int(oneobj.castreserv) // 5),
                                                        trakingcod = oneobj.rahgiricod,
                                                        bank= "zibal",
                                                        vahed=oneobj.vahed,
                                                        idwork=oneobj.idwork,
                                                        vaziyatereserv='قطعی',
                                                        bankpeyment="-1",
                    )
                    a = reservemodeltest.objects.filter(rahgiricod=rahgiricode)
                    a.delete()

                    users = accuntmodel.objects.all()
                    for user in users:
                        if int(user.melicode) == int (oneobj.mellicode) :
                            smstext = user.firstname+' '+ user.lastname + ' ' + 'عزیز' + '\n' + 'رزرو شما قطعی شد' + '\n' +'کد رهگیری پرداخت شما' + ' ' + rahgiricode +'\n' + 'با تشکر' + 'مطب دکتر اسدپور' + '\n' + '\n' + '\n' + 'لغو ارسال پیامک 11'
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

                    # requests.request('GET',"https://drmahdiasadpour.ir")
                    print('1')
                    print(oneobj.mellicode)
                    users = accuntmodel.objects.all()
                    for user in users:
                        if user.melicode == oneobj.mellicode :
                            user_login = authenticate(request,
                                                      username=user.melicode,
                                                      password=user.pasword,
                                                      )
                            if user_login is not None:
                                login(request, user_login)

                            return render(request,'new_end.html',
                                          context={
                                                                        "tracking_code":rahgiricode,
                                                                        }
                    )
        else:
            print('2')
            a = reservemodeltest.objects.filter(mellicode=request.user.username)
            a.delete()

            return redirect(ENDURL)

    else:
        print('3')
        a = reservemodeltest.objects.filter(mellicode=request.user.username)
        a.delete()

        return redirect(ENDURL)

def end(request):
    backbutton = request.GET.get('backbutton')
    if backbutton == "accept" :
        ur = f"{'http://127.0.0.1:8000'}/?{'r=33'}"
        return redirect(ur)

    message = f"دکتر_اسدپور_"

    try:
        api = KavenegarAPI(
            '527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D')
        params = {
            'receptor': "09122852099",
            'template': 'test',
            'token': message,
            'type': 'sms',
        }
        response = api.verify_lookup(params)
        return render(request, 'end.html', context={"result": 'endresult', })
    except APIException as e:
        m = 'tellerror'
        # messages.error(request,'در سیستم ارسال پیامک مشکلی پیش آمده لطفا شماره خود را به درستی وارد کنید و دوباره امتحان کنید در صورتی که مشکل برطرف نشد در اینستاگرام پیام دهید ')
        return render(request, 'end.html', context={"result": 'endresult', })
    except HTTPException as e:
        m = 'neterror'
        # messages.error(request,'در سیستم ارسال پیامک مشکلی پیش آمده لطفا شماره خود را به درستی وارد کنید و دوباره امتحان کنید در صورتی که مشکل برطرف نشد در اینستاگرام پیام دهید ')
        return render(request, 'add_cantact.html')
    return render(request, 'end.html', context={"result": 'endresult', })



def cast(request):
    peyment = request.POST.get("peyment")
    melicodevarizande = request.POST.get("melicodevarizande")
    detalejobselect = request.POST.get("detalejobselect")
    method =request.POST.get("method")
    persone = request.POST.get("persone")
    day = request.POST.get("day")
    mounth = request.POST.get("mounth")
    year = request.POST.get("year")
    select_job = request.POST.get("select_job")
    bankonvan = request.POST.get("bankonvan")
    pardakhtfaktor =request.POST.get("pardakhtfaktor")
    facebutton = request.POST.get("facebutton")
    faceb1 = request.POST.get("faceb1")
    off = request.POST.get("off")
    beyane = request.POST.get("beyane")
    offer = request.POST.get("offer")
    inputsearchname = ''
    selectfile = request.POST.get("selectfile")
    melifaktorinput = request.POST.get("melifaktorinput")
    facesearchmelicode = request.POST.get("facesearchmelicode")
    melicodsearch = request.POST.get("melicodsearch")
    namesearch= request.POST.get("namesearch")
    facebuttonsearchname = request.POST.get("facebuttonsearchname")
    buttomteakclick = request.POST.get("buttomteakclick")
    bankonvanfavtor = request.POST.get('bankonvanfavtor')
    tickon = request.POST.get('tickon')
    ia = request.POST.get("ia")
    jamekol = request.POST.get('jamekol')
    offerbuttom = request.POST.get("offerbuttom")
    inputid = request.POST.get("inputid")
    offermeghdar =request.POST.get("offermeghdar")
    beyanemeghdar= request.POST.get("beyanemeghdar")
    namesearch = request.POST.get("namesearch")
    meliinput = request.POST.get("meliinput")
    selectjob = request.POST.get("select_job")
    searchnamebottum = request.POST.get("searchnamebottum")
    # pardakhtfaktor = request.POST.get("pardakhtfaktor")
    melicodvarizande =request.POST.get("melicodvarizande")
    jamekolinput = request.POST.get('jamekolinput')
    bankonvanfactor = request.POST.get("bankonvanfactor")
    bankpey = request.POST.get("bankpey")
    jamkol = 0




    # *******************لیست حسابها رو در میار و در آرایه methodpardakht میریزه***********
    bs = bankmodel.objects.all()
    methodpardakht = ['']
    methodpardakht.clear()
    for b in bs:
        methodpardakht.append(b.onvan)



    # -------------------------------------------------------------- برسی بیعانه برای این خدمت---
    beys = reservemodel.objects.all()
    beyane = 0
    for bey in beys:
        if (bey.melicod ==  melicodevarizande) and (bey.checking == 'false'):
            beyane = beyane + int(bey.pyment)




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



# ---------------------------------------------------------------------------لیست کارها در jobs-----
    works = workmodel.objects.all()
    s = ""
    jobs = [""]
    jobs.clear()
    for work in works:
        r = 0
        for job in jobs :
            if job ==  work.work :
                r = 1
                break
        if r == 0 :
            jobs.append(work.work +" "+ work.detalework+" "+work.person)





# --------------------------------------------------------------------------------------- 31 روز رو میریزه توی darray----
    t = datetime.datetime.now()
    d = strd(t)
    y = str(1400 + int(stry(t)))
    m = strb(t)
    darrey = [1]

    darrey.clear()
    darrey.append(d)
    de = "1"
    while   int(de) <= 31 :
        darrey.append(de)
        de = str(int(de) + 1)



# -----------ماه ها رو میریزه توی marray--------
    marrray = [m]
    marrray.clear()
    marrray.append(m)
    tt = datetime.datetime.now()
    m1 = m
    m2 = m
    while m1 == m :
        tt -= timedelta(days=1)
        m1 = strb(tt)
        if m1 != m :
            marrray.append(m1)
            m = m1
            if m2 == m1 :
                break



# ---------سالها رو میریزه توی yarry-------------
    yarray = [1]
    yarray.clear()
    while int(y) > 1300 :
        yarray.append(int(y))
        y = str(int(y)-1)
    us = accuntmodel.objects.all()



    etebarmelicod = "true"
    cash = 0
    selectjob = "انتخاب کنید"
    codemeli = ""
    if faceb1 == "accept" :
        etebarmelicod = "false"
        for u in us:
            if u.melicode == melicodevarizande:
                etebarmelicod = "true"
                codemeli = melicodevarizande
    if facebutton == "accept" :
        codemeli = melicodevarizande
        cs = casttestmodel.objects.all()
        for j in cs:
            j.delete()
        js = workmodel.objects.all()
        for j in js :
            if (jobs[int(selectjob)] == j.work +" "+ j.detalework+" "+j.person ) :
                cash = j.cast
                sjb = j.work +" "+ j.detalework
                persone =j.person
        selectjob = sjb
        casttestmodel.objects.create(
            p=cash,
            s=selectjob,
            c=persone,
        )
    etebarsabt = "notr"
    if pardakhtfaktor == "accept":
        rs = fpeseshktestmodel.objects.all()
        for r in rs :
            cs = ctmodel.objects.all()
            if (int(melicodvarizande) == int(r.melicod)) and (r.checking != 'true') :
                et = "true"
                for c in cs:
                    if int(r.id) == int(c.idf) :
                        et = "false"
                zz = ''
                banks = bankmodel.objects.all()
                for bb in banks :
                    if int(bb.id) == int(bankonvanfactor) :
                        zz = bb.onvan
                if et == 'true':
                    castmodel.objects.create(
                    idf = r.id,
                    melicodvarizande = r.melicod,
                    dateshamsi = stradby(datetime.datetime.now()),
                    datemiladi = datetime.datetime.now().strftime('%a %d %b %y'),
                    filenumber = datetime.datetime.now().strftime('%a %d %b %y') + ',' +str(melicodvarizande),
                    cashmethodid = str(bankonvanfactor),
                    cashmethodname = zz,
                    melicodeoperatore = request.user.username,
                    mablagh = str(jamekolinput),
                    bankpeyment=r.bankpeyment,
                    )
                    a =fpeseshktestmodel.objects.filter(id=int(r.id))
                    a.update(checking='true')

        etebarsabt = 'true'
    arrayname = ['']
    arrayname.clear()
    etebarname = "notr"
    name = ''
    jamkol = 0
    mtick = ''
    nselect = ''
    mselect = ''
    reserv = ['']
    reserv.clear()
    ls = listmodeltest.objects.all()
    if (tickon != None) and (tickon != ''):
        inttikon = int(tickon)
        ar = ['']
        ar.clear()
        for l in ls :
            ar.append(l.m)
        # -- چون سرور بر عکس ترتیه ها رو میخونه ایمچا و در reserv,view.reservdasti این کامنت هست-
        ar.reverse()
        mtick = ar[inttikon]
        a = ctmodel.objects.filter(melicod=str(mtick))
        a.delete()
    if buttomteakclick == "accept":
        us = accuntmodel.objects.all()
        for u in us:
            if int(u.melicode) == int(mtick) :
                nselect = u.firstname + " " + u.lastname
                mselect = u.melicode
        fs = fpeseshktestmodel.objects.all()
        for f in fs :
            if (int(f.melicod) == int(mtick)) and (f.checking != 'true'):
                r = ['']
                r.clear()
                r.append(f.jobreserv + ' '+ f.detalereserv)
                r.append(f.dateshamsireserv)
                r.append(f.castreserv)
                r.append(f.pyment)
                r.append(f.offer)
                r.append(f.id)
                jamkol = jamkol + float(f.castreserv) - float(f.pyment) - float(f.offer)
                reserv.append(r)
        bs = bankmodel.objects.all()
        methodpardakht = ['']
        methodpardakht.clear()
        for b in bs :
            methodpardakht.append(b.onvan)

        return render(request,'faktor.html',context={
            'name': nselect,
            'melicode':mselect,
            'reserv':reserv,
            'jamkol':int(jamkol),
            'bank':hesabs,
            'melicodvarizande':mtick,
        })
    na = ''
    if (offer != None) and (offer != ''):
        qs = fpeseshktestmodel.objects.all()
        for q in qs:
            if str(q.id) == str(offer):
                uses = accuntmodel.objects.all()
                for use in uses:
                    if use.melicode == q.melicod :
                        na = use.firstname + ' ' + use.lastname
                return render(request,'offer.html',context={
                    'name':na,
                    'pracedure':q.jobreserv + ' ' + q.detalereserv,
                    'cast':q.castreserv,
                    'peyment':q.pyment,
                    'offer':q.offer,
                    'id':q.id,
                    'melicodvarizande':melicodvarizande,
                    'bank': hesabs,
                })
    if offerbuttom == 'accept':
        if (inputid != None) and ( inputid != ''):
            a = fpeseshktestmodel.objects.filter(id=int(inputid))
            if (offermeghdar != None) and (offermeghdar != ''):
                a.update(offer=offermeghdar)
            if (beyanemeghdar != None)  and (beyanemeghdar != ''):
                yu = int(bankpey)
                a.update(pyment=beyanemeghdar,bankpeyment=bankpey)
        us = accuntmodel.objects.all()
        for u in us:
            if int(u.melicode) == int(melicodvarizande) :
                nselect = u.firstname + " " + u.lastname
                mselect = u.melicode
        fs = fpeseshktestmodel.objects.all()
        for f in fs :
            if (int(f.melicod) == int(melicodvarizande)) and (f.checking != 'true'):
                r = ['']
                r.clear()
                r.append(f.jobreserv + ' '+ f.detalereserv)
                r.append(f.dateshamsireserv)
                r.append(f.castreserv)
                r.append(f.pyment)
                r.append(f.offer)
                r.append(f.id)
                jamkol = jamkol + float(f.castreserv) - float(f.pyment) - float(f.offer)
                reserv.append(r)
        bs = bankmodel.objects.all()
        methodpardakht = ['']
        methodpardakht.clear()
        for b in bs :
            methodpardakht.append(b.onvan)
        return render(request,'faktor.html',context={
            'name': nselect,
            'melicode':mselect,
            'reserv':reserv,
            'jamkol':int(jamkol),
            'bank':hesabs,
            'melicodvarizande':melicodvarizande,
        })
    if facesearchmelicode == "accept":
        etebarname = "false"
        us = accuntmodel.objects.all()
        for u in us:
            ls = listmodeltest.objects.all()
            for l in ls:
                a = listmodeltest.objects.filter(m=l.m)
                a.delete()
            ar = ['']
            ar.clear()
            if melicodsearch == u.melicode :
                ar.append(u.firstname + " " + u.lastname)
                ar.append(u.melicode)
                listmodeltest.objects.create(m=a.melicode)
                arrayname.append(ar)
                etebarname = "true"
    if (selectfile != None) and (selectfile != ''):
        jamkol = 0
        users = accuntmodel.objects.all()
        for user in users:
            if user.melicode == int(melicodvarizande):
                name = user.firstname + ' ' + user.lastname
        rs = fpeseshktestmodel.objects.all()
        reserv = ['']
        reserv.clear()
        for r in rs :
            reserarray = ['']
            reserarray.clear()
            cs = ctmodel.objects.all()
            if (int(melicodvarizande) == int(r.melicod)) and (r.checking != 'true') :
                et = "true"
                for c in cs:
                    if int(r.id) == int(c.idf) :
                        et = "false"
                if et == 'true':
                    reserarray.append(r.jobreserv + " " + r.detalereserv)
                    reserarray.append(r.dateshamsireserv)
                    reserarray.append(r.castreserv)
                    reserarray.append(r.pyment)
                    reserarray.append(r.offer)
                    reserarray.append(r.id)
                    jm = float(jamkol) + float(r.castreserv) - float(r.pyment) - float(r.offer)
                    jamkol =int(jm)
                    reserv.append(reserarray)
        jjm = float(jamkol) - float(reserv[int(selectfile)][2]) + float(reserv[int(selectfile)][3]) + float(reserv[int(selectfile)][4])
        jamkol = int(jjm)
        ctmodel.objects.create(idf=reserv[int(selectfile)][5],melicod=str(melicodvarizande))
        reserv.pop(int(selectfile))
        return render(request,'faktor.html',context={
                                                                    "reserv":reserv,
                                                                    'melicode':melifaktorinput,
                                                                    'name':name,
                                                                    'bank':hesabs,
                                                                    'jamkol':jamkol,
                                                                    'melicodvarizande':melicodvarizande,
        })
    if namesearch == None :
        namesearch = ''
    if searchnamebottum == 'accept':
        ls = listmodeltest.objects.all()
        for l in ls:
            a = listmodeltest.objects.filter(m=l.m)
            a.delete()
        arrayname.clear()

        auser = accuntmodel.objects.all()
        amarray =['']
        amarray.clear()
        for uss in auser:
            if uss.firstname[0:3] == namesearch :
                mm = ['']
                mm.clear()
                mm.append(uss.firstname + " " + uss.lastname)
                mm.append(uss.melicode)
                amarray.append(uss.melicode)
                listmodeltest.objects.create(m=uss.melicode)
                arrayname.append(mm)
        for aa in auser:
            if aa.lastname[0:3] == namesearch :
                cheek = "true"
                for archek in amarray:
                    if archek == aa.melicode :
                        cheek = "false"
                if cheek == "true" :
                    mm = ['']
                    mm.clear()
                    mm.append(aa.firstname + " " + aa.lastname)
                    mm.append(aa.melicode)
                    listmodeltest.objects.create(m=aa.melicode)
                    arrayname.append(mm)
    return render(request,'cast_searchname.html',context={
                                                                        "inputsearchname":inputsearchname,
                                                                        "melicode":melicodsearch,
                                                                        "arrayname":arrayname,
                                                                        "etebarname":etebarname,
                                                                        'searchinput':namesearch,
                                                                        's':ia,
                                                                        'etebarsabt':etebarsabt,
                                                                        'bank': hesabs,
    })

def banksave(request):
    onvan = request.POST.get("onvan")
    officnamber = request.POST.get("officnamber")
    namberkart = request.POST.get("namberkart")
    shebanamber = request.POST.get("shebanamber")
    melicodebank = request.POST.get("melicodebank")
    interky = request.POST.get("interky")
    if interky == "accept":
        bankmodel.objects.create(onvan=onvan,officnamber=officnamber,namberkart=namberkart,
                                  shebanamber=shebanamber,melicodebank=melicodebank,)
    return render(request,'bank.html')

def pardakhtdef(request):
    factorn = request.POST.get("factorn")
    button_factor =  request.POST.get("button_factor")
    doc_time = request.POST.get("doc_time")
    doc_material= request.POST.get("doc_material")
    doc_forosh = request.POST.get("doc_forosh")
    doc_factor= request.POST.get("doc_factor")
    ciliktime = 'false'
    if doc_time == 'accept' :
        ciliktime = "true"
    cilikmaterial = 'false'
    if doc_material == 'accept' :
        cilikmaterial = "true"
    cilikfactor = 'false'
    if doc_factor == 'accept' :
        cilikfactor = "true"
    cilikforosh = 'false'
    if doc_forosh == 'accept' :
        cilikforosh = "true"

    yearcant = [0]
    yearcant.clear()
    tyear = datetime.datetime.now()
    h = int(stry(tyear))+1400
    while 1300 <= h :
        yearcant.append(str(h))
        h -= 1



    ws = waremodel.objects.all()
    flist = ['']
    flist.clear()
    for ww in ws:
        try:
            if (ww.kala != '') and (ww.kala != None) :
                flist.append(ww.id)
        except:
            print("error the pardakht")
            
    factors = ['']
    factors.clear()
    baghimande = 0
    bestankari = 0
    bedehkari = 0
    jamkool = 0
    idfroshande = 0
    if button_factor == 'accept':
        if (factorn != '') and (factorn != None):
            for w in ws:
                if str(w.factornumber) == str(factorn):
                    factor=['']
                    factor.clear()
                    factor.append(w.day+'/'+w.mounth+'/'+w.year)
                    es = esmekalamodel.objects.all()
                    for e in es :
                        if str(e.id) == str(w.kala):
                            factor.append(e.esmekala)
                    factor.append(w.cast)
                    factor.append(w.takhfif)
                    fs = froshandemodel.objects.all()
                    for f in fs :
                        if str(f.id) == str(w.froshande):
                            factor.append(f.firstname+' '+f.lastname)
                            idfroshande = f.id
                    if w.pardakht == "1":
                        factor.append("پرداخت شده")
                    if w.pardakht == "0":
                        factor.append("پرداخت نشده")
                    if w.tahvil == "1":
                        factor.append("تحویل انبار شده")
                    if w.tahvil == "0":
                        factor.append("تحویل  انبار نشده")

                    jamkool = jamkool + int(w.cast) - int(w.takhfif)
                    factors.append(factor)

        for w in ws:
            if int(w.froshande) == int(idfroshande) :
                bedehkari = bedehkari + int(w.cast) - int(w.takhfif)
        baghimande = bedehkari - bestankari
        bedehkari = bedehkari - jamkool
        return render(request,'factorlist.html',context={
            'factors':factors,
            'baghimande':baghimande,
            'bestankari':bestankari,
            'bedehkari':bedehkari,
            'jamkool':jamkool,
        })
    return render(request,'pardakht.html', context={
        'ciliktime':ciliktime,
        'cilikmaterial':cilikmaterial,
        'cilikfactor':cilikfactor,
        'cilikforosh':cilikforosh,
        'yearcant':yearcant,
         })

def closecashdef(request):
    castbeyane = request.POST.get("castbeyane")
    castoffer = request.POST.get("castoffer")
    bankonvanedit = request.POST.get("bankonvanedit")
    dayedit = request.POST.get("dayedit")
    mounthedit = request.POST.get("mounthedit")
    idfpedit = request.POST.get("idfpedit")
    idcedit = request.POST.get("idcedit")
    buttonedit = request.POST.get("buttonedit")
    buttondelet = request.POST.get("buttondelet")
    cash = request.POST.get("cash")
    closecash = request.POST.get("closecash")
    day = request.POST.get("day")
    daysave = request.POST.get("daysave")
    bankpey = request.POST.get("bankpey")
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


    m = request.user.username
    users = accuntmodel.objects.all()
    level =''
    for user in users:
        if user.melicode == m :
            level = user.level


    if (day == None) or (day == '') or (day == "None") :
        day = daysave
    if day == None :
        day = ''

    mounth = request.POST.get("mounth")
    mounthsave = request.POST.get("mounthsave")
    if (mounth == None) or (mounth == '') or (mounth == "None") :
        mounth = mounthsave
    if mounth == None :
        mounth = ''


    t = datetime.datetime.now()
    while strb(t) != 'فروردین' :
        t -= timedelta(days=28)
    while strd(t) != "1" :
        t -= timedelta(days=1)
    if (mounth != '') and (day != ''):
        while strb(t) != mounth :
            t += timedelta(days=1)
        while strd(t) != day :
            t += timedelta(days=1)


    casts = castmodel.objects.all()
    casharray = ['']
    casharray.clear()
    castid = 0
    for cast in casts:
        if cast.datemiladi == t.strftime('%a %d %b %y'):
            namecast = ''
            users = accuntmodel.objects.all()
            for user in users:
                if int(user.melicode) == int(cast.melicodvarizande):
                    namecast = user.firstname + " " + user.lastname
            jobcast = ''
            datecast = ''
            fs = fpeseshktestmodel.objects.all()
            mablagh = 0
            for f in fs:
                if int(f.id) == int(cast.idf):
                    castid = cast.id
                    jobcast = f.jobreserv + " " + f.detalereserv
                    datecast= f.dateshamsireserv
                    mablagh = str(int(float(f.castreserv) - float(f.pyment) - float(f.offer)))
            carray = ['']
            carray.clear()
            carray.append(namecast)
            carray.append(jobcast)
            carray.append(datecast)
            carray.append(mablagh)
            carray.append(cast.cashmethodname)
            carray.append(cast.idf)
            carray.append(cast.cashmethodid)
            casharray.append(carray)

    mablaghkol = 0
    bankarray = ['']
    bankarray.clear()
    bankarray.append(["0","b",0])
    bankonvan = ''
    melicodbank =''
    idc = 0
    for c in casharray:
        idc = int(c[6])
        ete = 'true'

        if len(bankarray) > 0 :
            for a in bankarray :
                if int(a[2]) == idc :
                    ete = 'false'
        if ete != 'false' :
            banks = bankmodel.objects.all()
            for bank in banks:
                if int(bank.id) == idc:
                    bankonvan = bank.onvan
                    melicodbank = bank.melicodebank
            mablaghkol = 0
            for b in casharray :
                if int(b[6]) == idc:
                    mablaghkol = mablaghkol + int(b[3])
            barray = ['']
            barray.clear()
            barray.append(mablaghkol)
            barray.append(bankonvan)
            barray.append(idc)
            barray.append(melicodbank)
            bankarray.append(barray)
    jam = 0
    for q in bankarray:
        jam = int(float(q[0]) + float(jam))
    bankarray.append([jam,'جمع کل',0,'3257525958'])
    del bankarray[0]
    if closecash == 'accept':
        if 1==1:
            if len(bankarray) > 0:
                for a in bankarray:
                    bs = bankmodel.objects.all()
                    users = accuntmodel.objects.all()
                    for user in users:
                        if int(user.melicode) == int(a[3]) :
                            sms = "با سلام جمع صندوق تاریخ" + " " + strd(t) +strb(t) +' ' + "مبلغ" +' '+ str(a[0]) + " " + " واریز به حساب"+ " " + str(a[1])
                            try:
                                api = KavenegarAPI(
                                    '527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D')
                                params = {
                                    'sender': '9982003178',  # optional
                                    'receptor': user.phonnumber,  # multiple mobile number, split by comma
                                    'message': sms,
                                }
                                response = api.sms_send(params)
                                # return render(request, 'code_cantact.html')
                            except APIException as e:
                                m = 'tellerror'
                                return render(request, 'closecash.html', context={'melicod_etebar': m})
                            except HTTPException as e:
                                m = 'neterror'
                                return render(request, 'closecash.html', context={'melicod_etebar': m}, )
                return redirect('/')
    if (cash != '') and (cash != None) and (cash != 'None') :
        fpeseshks = fpeseshktestmodel.objects.all()
        cas = castmodel.objects.all()
        name = ''
        job = ''
        castjob = ''
        castbeyane =''
        castoffer =''
        idcast = 0
        idfp = 0
        for fpeseshk in fpeseshks:
            if int(fpeseshk.id) == int(cash):
                idfp = fpeseshk.id
                for ca in cas:
                    if int(ca.idf) == int(fpeseshk.id) :
                        idcast = ca.id
                users = accuntmodel.objects.all()
                for user in users:
                    if int(user.melicode) == int(fpeseshk.melicod):
                        name = user.firstname + " " + user.lastname
                job = fpeseshk.jobreserv + ' ' + fpeseshk.detalereserv
                castjob = fpeseshk.castreserv
                castbeyane = fpeseshk.pyment
                castoffer = fpeseshk.offer

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

        return render(request,'new_cash.html',context={
            'name':name,
            'job':job,
            'castjob':castjob,
            'castbeyane':castbeyane,
            'castoffer':castoffer,
            'hesabs':hesabs,
            'idc':idcast,
            'idfp':idfp,
            'bank': hesabs,
        })
    if buttondelet == 'accept' :
        a=castmodel.objects.filter(id=int(idcedit))
        b=fpeseshktestmodel.objects.filter(id=int(idfpedit))
        a.delete()
        b.update(checking='false',offer=0,pyment=0)
    if buttonedit == 'accept':
        yu = int(bankpey)
        tedit = datetime.datetime.now()
        while strb(tedit) != 'فروردین':
            tedit -= timedelta(days=28)
        while strd(tedit) != "1":
            tedit -= timedelta(days=1)
        if (mounthedit != '') and (dayedit != '') and (mounthedit != None) and (dayedit != None) and (mounthedit != 'None') and (dayedit != 'None'):
            while strb(tedit) != mounthedit:
                tedit += timedelta(days=1)
            while strd(tedit) != dayedit:
                tedit += timedelta(days=1)
        zz = ''
        banks = bankmodel.objects.all()
        for bb in banks:
            if int(bb.id) == int(bankonvanedit):
                zz = bb.onvan

        a=castmodel.objects.filter(id=int(idcedit))
        b=fpeseshktestmodel.objects.filter(id=int(idfpedit))
        a.delete()
        b.update(offer=castoffer,pyment=castbeyane,bankpeyment=bankpey)
        fps = fpeseshktestmodel.objects.all()
        for fp in fps:
            if int(fp.id) == int(idfpedit):
                j = str(int(float(fp.castreserv) - float(fp.offer) - float(fp.pyment)))
                castmodel.objects.create(
                    idf=fp.id,
                    melicodvarizande=fp.melicod,
                    dateshamsi=stradby(tedit),
                    datemiladi= tedit.strftime('%a %d %b %y'),
                    filenumber= tedit.strftime('%a %d %b %y') + ',' + str(fp.melicod),
                    cashmethodid=str(bankonvanedit),
                    cashmethodname=zz,
                    melicodeoperatore=request.user.username,
                    mablagh=j,
                    dateshamsieditor=stradby(datetime.datetime.now()),
                    bankpeyment=bankpey,
                )

    return render(request,'closecash.html',context={
        'day':day,
        'mounth': mounth,
        'rarray':casharray,
        'bankarray':bankarray,
        'level':level,
        'bank': hesabs,
    })


def contact(request):
    number = request.POST.get('number')
    delet =request.POST.get('delet')
    users = accuntmodel.objects.all()
    name =''
    if (number != '') and (number != None):
        for i in users :
            try:
                if int(i.phonnumber) == int(number) :
                    name = i.firstname+ '  ' + i.lastname
            except:
                print("error for phon number")
    if (delet == 'accept') and (number != '') and (number != None):
        a = accuntmodel.objects.filter(phonnumber=number)
        a.delete()

    return render(request,'contact.html', context={
                                                                "name":name,
                                                                "number":number,
                                                                    })


def hesabsazi(request):
    fs = froshandemodel.objects.all()
    frosharray = ['']
    frosharray.clear()
    for f in fs :
        frosharray.append([f.firstname+' '+f.lastname,f.id])
    name =request.POST.get('name')
    onvan = request.POST.get('onvan')
    officnamber = request.POST.get('officnamber')
    namberkart = request.POST.get('namberkart')
    shebanamber = request.POST.get('shebanamber')
    interky = request.POST.get('interky')
    if interky == 'accept':
        hesab.objects.create(
            onvansherkat=onvan,
            shomarehesabd=officnamber,
            shomarekart=namberkart,
            shomaresheba=shebanamber,
            idfroshander= name,
        )
    return render(request, 'hesabdaryaft.html',context={
        'frosharray':frosharray,
    })

