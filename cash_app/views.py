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
from reserv_app.models import reservemodeltest,reservemodel
from jobs_app.models import jobsmodel,employeemodel,workmodel
from cash_app.models import bankmodel,castmodel,casttestmodel,listmodeltest
from cantact_app.models import accuntmodel
from cantact_app.views import *
from file_app.models import fpeseshktestmodel
ZIB_API_REQUEST = "https://gateway.zibal.ir/v1/request"
ZIB_API_VERIFY = "https://gateway.zibal.ir/verify"
ZIB_API_STARTPAY = "https://gateway.zibal.ir/start/"
ZIB_API_TOKEN = 'https://gateway.zibal.ir/v1/verify'

callbackzibalurl = 'http://127.0.0.1:8000/zib/verifyzibal/'
merchanzibal = 'zibal'
ENDURL = "http://127.0.0.1:8000"

# ENDURL = "https://drmahdiasadpour.ir"
# callbackzibalurl = 'https://drmahdiasadpour.ir/zib/verifyzibal/'
# merchanzibal = '64c2047fcbbc270017f4c6b2'

def orderzibal(request):
    peyment = 50000
    phonnumber = "0"
    if request.user.is_authenticated:
        allmodel = reservemodeltest.objects.all()
        for oneobject in allmodel:
            if oneobject.mellicode == request.user.username :
                peyment = int(oneobject.castreserv) // 5
                phonnumber = str(oneobject.phonnumber)
        data = {
            "merchant": merchanzibal,
            "amount": peyment,
            "callbackUrl": callbackzibalurl,
            "description": "بیعانه جهت رزرو",
            "orderId": "ZBL-7799",
            "mobile": phonnumber
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        res = requests.post(ZIB_API_REQUEST, data=data, headers=headers)
        r = res.json()
        if res.status_code == 200:
            if r['result'] == 100:
                a = reservemodeltest.objects.filter(mellicode=request.user.username)
                a.update(rahgiricod=str(r['trackId']))
                url = f"{ZIB_API_STARTPAY}{r['trackId']}"
                return redirect(url)
        else:
            return HttpResponse(str(res.json()['errors']))


def callbackzibal(request):
    backbutton = request.GET.get('backbutton')
    if (backbutton != "") and (backbutton != None) :
        ur = f"{ENDURL}/?r={backbutton}"
        # ur = ENDURL
        return redirect(ur)

    trac = request.GET['trackId']
    data = {
        "merchant": merchanzibal,
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
                                                        )
                    a = reservemodeltest.objects.filter(rahgiricod=rahgiricode)
                    a.delete()
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
                        # response = api.verify_lookup(params)
                        # return render(request, 'end.html', context={"result": 'endresult', })
                    except APIException as e:
                        m = 'tellerror'
                        # messages.error(request,'در سیستم ارسال پیامک مشکلی پیش آمده لطفا شماره خود را به درستی وارد کنید و دوباره امتحان کنید در صورتی که مشکل برطرف نشد در اینستاگرام پیام دهید ')
                        return render(request, 'end.html', context={"result": 'endresult', })
                    except HTTPException as e:
                        m = 'neterror'
                        # messages.error(request,'در سیستم ارسال پیامک مشکلی پیش آمده لطفا شماره خود را به درستی وارد کنید و دوباره امتحان کنید در صورتی که مشکل برطرف نشد در اینستاگرام پیام دهید ')
                        # return render(request, 'add_cantact.html')
                        return render(request, 'end.html', context={"result": 'endresult', })

                    # requests.request('GET',"https://drmahdiasadpour.ir")
                    return render(request,'end.html',context={
                                                                "firstname":firstname,
                                                                "lastname":lastname,
                                                                "rahgiricode":rahgiricode,
                                                                "kolkhedmat":kolkhedmat,
                                                                "day":day,
                                                                "houre":houre,
                                                                })
        else:
            a = reservemodeltest.objects.filter(mellicode=request.user.username)
            a.delete()

            return redirect(ENDURL)

    else:
        a = reservemodeltest.objects.filter(mellicode=request.user.username)
        a.delete()

        return redirect(ENDURL)

def end(request):
    # backbutton = request.GET.get('backbutton')
    # if backbutton == "accept" :
    #     ur = f"{'http://127.0.0.1:8000'}/?{'r=33'}"
    #     return redirect(ur)

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
        # return render(request, 'add_cantact.html')
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
    pardakhtfaktor = request.POST.get("pardakhtfaktor")
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
    b = ""
    hesabs = [""]
    hesabs.clear()
    for bank in banks:
        r = 0
        for hesab in hesabs :
            if hesab ==  bank.onvan :
                r = 1
                break
        if r == 0 :
            hesabs.append(bank.onvan)
    if (bankonvan != None) and (bankonvan != ""):
        b = hesabs[int(bankonvan)]




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
        a = fpeseshktestmodel.objects.filter(melicod=melifaktorinput)
        a.update(checking='true')
        rs = fpeseshktestmodel.objects.all()
        for r in rs :
            if melifaktorinput == r.melicod :
                castmodel.objects.create(
                idf = r.id,
                melicodvarizande = r.melicod,
                dateshamsi = stradby(datetime.datetime.now()),
                datemiladi = datetime.datetime.now().strftime('%a %d %b %y'),
                filenumber = datetime.datetime.now().strftime('%a %d %b %y') + ',' +melifaktorinput,
                cashmethod = b,
                melicodeoperatore = request.user.username,
                mablagh = str(jamekol),
                )
                etebarsabt = 'true'



    arrayname = ['']
    arrayname.clear()
    etebarname = "notr"
    name = ''
    jamkol = 0
    if (tickon != None) and (tickon != ''):
        inttikon = int(tickon)
    ls = listmodeltest.objects.all()
    mtick = ''
    nselect = ''
    mselect = ''
    reserv = ['']
    reserv.clear()
    if buttomteakclick == "accept":
        for l in ls :
            if inttikon == 0 :
                mtick = l.m
                break
            inttikon = inttikon - 1
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
            'bank':methodpardakht,
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
                    'id':q.id,
                })


    if offerbuttom == 'accept':
        if (inputid != None) and ( inputid != ''):
            a = fpeseshktestmodel.objects.filter(id=int(inputid))
            if (offermeghdar != None) and (offermeghdar != ''):
                a.update(offer=offermeghdar)
            if (beyanemeghdar != None)  and (beyanemeghdar != ''):
                a.update(pyment=beyanemeghdar)




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
            if user.melicode == melifaktorinput:
                name = user.firstname + ' ' + user.lastname
        rs = fpeseshktestmodel.objects.all()
        reserv = ['']
        reserv.clear()
        for r in rs :
            reserarray = ['']
            reserarray.clear()
            if (melifaktorinput == r.melicod) and (r.checking != 'true') :
                reserarray.append(r.jobreserv + " " + r.detalereserv)
                reserarray.append(r.dateshamsireserv)
                reserarray.append(r.castreserv)
                reserarray.append(r.pyment)
                reserarray.append(r.offer)
                reserarray.append(r.id)
                jm = float(jamkol) + float(r.castreserv) - float(r.pyment) - float(r.offer)
                jamkol =int(jm)
                reserv.append(reserarray)

        idw = reserv[int(selectfile)][5]
        fs = fpeseshktestmodel.objects.all()
        for f in fs :
            if int(f.id) == int(idw):
                reservemodel.objects.create(
                    melicod=f.melicod,
                    jobreserv = f.jobreserv,
                    detalereserv = f.detalereserv,
                    personreserv = f.personreserv,
                    timereserv = f.timereserv,
                    castreserv = f.castreserv,
                    numbertime = f.numbertime,
                    hourreserv = f.hourreserv,
                    dateshamsireserv = f.dateshamsireserv,
                    datemiladireserv = f.datemiladireserv,
                    yearshamsi = f.yearshamsi,
                    cardnumber = f.cardnumber,
                    pyment = f.pyment,
                    trakingcod = f.trakingcod,
                    bank = f.bank,
                    checking = f.checking,
                    vahed = f.vahedeobjectname,
                                                )
                a = fpeseshktestmodel.objects.filter(id=int(idw))
                a.delete()
        jjm = float(jamkol) - float(reserv[int(selectfile)][2]) + float(reserv[int(selectfile)][3]) + float(reserv[int(selectfile)][4])
        jamkol = int(jjm)
        reserv.pop(int(selectfile))
        return render(request,'faktor.html',context={
                                                                    "reserv":reserv,
                                                                    'melicode':melifaktorinput,
                                                                    'name':name,
                                                                    'bank':methodpardakht,
                                                                    'jamkol':jamkol,
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
        for uss in auser:
            if uss.firstname[0:3] == namesearch :
                mm = ['']
                mm.clear()
                mm.append(uss.firstname + " " + uss.lastname)
                mm.append(uss.melicode)
                listmodeltest.objects.create(m=uss.melicode)
                arrayname.append(mm)
        for aa in auser:
            if aa.lastname[0:3] == namesearch :
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

def pardakht(request):
    return render(request,'pardakht.html')