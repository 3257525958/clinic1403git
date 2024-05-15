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
from cash_app.models import bankmodel,castmodel
from cantact_app.models import accuntmodel
ZIB_API_REQUEST = "https://gateway.zibal.ir/v1/request"
ZIB_API_VERIFY = "https://gateway.zibal.ir/verify"
ZIB_API_STARTPAY = "https://gateway.zibal.ir/start/"
ZIB_API_TOKEN = 'https://gateway.zibal.ir/v1/verify'

# callbackzibalurl = 'http://127.0.0.1:8000/zib/verifyzibal/'
# merchanzibal = 'zibal'
# ENDURL = "http://127.0.0.1:8000"

ENDURL = "https://drmahdiasadpour.ir"
callbackzibalurl = 'https://drmahdiasadpour.ir/zib/verifyzibal/'
merchanzibal = '64c2047fcbbc270017f4c6b2'

def orderzibal(request):
    peyment = 50000
    phonnumber = "0"
    if request.user.is_authenticated:
        allmodel = reservemodeltest.objects.all()
        for oneobject in allmodel:
            if oneobject.mellicode == request.user.username :
                peyment = int(oneobject.castreserv)
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
                                                        pyment=oneobj.castreserv,
                                                        trakingcod = oneobj.rahgiricod,
                                                        bank= "zibal"
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
            return redirect(ENDURL)

    else:
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
    # facebutton = request.POST.get("facebutton")
    # if facebutton == "accept":
    peyment = request.POST.get("peyment")
    melicodevarizande = request.POST.get("melicodevarizande")
    detalejobselect = request.POST.get("detalejobselect")
    method =request.POST.get("method")
    select_persone = request.POST.get("persone")
    day = request.POST.get("day")
    mounth = request.POST.get("mounth")
    year = request.POST.get("year")
    select_job = request.POST.get("select_job")
    bankonvan = request.POST.get("bankonvan")
    savebottom =request.POST.get("savebottom")
    facebutton = request.POST.get("facebutton")

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
            jobs.append(work.work +" "+ work.detalework)


    if (select_job != None) and (select_job != ""):
        s = jobs[int(select_job)]


    works = workmodel.objects.all()
    p = ""
    persons = [""]
    persons.clear()
    for work in works:
        r = 0
        for person in persons :
            if person ==  work.person :
                r = 1
                break
        if r == 0 :
            persons.append(work.person)
    if (select_persone != None) and (select_persone != ""):
        p = persons[int(select_persone)]



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

    yarray = [1]
    yarray.clear()
    while int(y) > 1300 :
        yarray.append(int(y))
        y = str(int(y)-1)
    us = accuntmodel.objects.all()
    etebarmelicod = "false"
    for u in us:
        if u.melicode == melicodevarizande :
            etebarmelicod = "true"



    cash = 0
    selectjob = "انتخاب کنید"
    if facebutton == "accept" :
        selectjob = request.POST.get("select_job")
        js = workmodel.objects.all()
        for j in js :
            if (jobs[int(selectjob)] == j.work +" "+ j.detalework ) :
                cash = j.cast
                sjb = j.work +" "+ j.detalework
        selectjob = sjb

    if (savebottom == "accept") and (etebarmelicod == "true"):
        operatore = request.user.username
        castmodel.objects.create(peyment=peyment,melicodevarizande=melicodevarizande,selectjob=select_job,bankonvan=bankonvan,
                                 person=person,operatore=operatore,day=day,mounth=mounth,year=year)
    g = "3200"

    return render(request,'cast_form.html',context={
                                                                 "selectjob":selectjob,
                                                                 # "listofperson": listofperson,
                                                                 "g":g,
                                                                 "jobs":jobs,
                                                                 "persons":persons,
                                                                 # "detaleworks":detaleworks,
                                                                 # "select_job":select_job,
                                                                 # "jobselect":s,
                                                                 # " melicode": mel,
                                                                 "cash":cash,
                                                                 "yarray":yarray,
                                                                 "darrey":darrey,
                                                                 "marray":marrray,
                                                                 "hesabs":hesabs,
                                                                 "etebarmelicod":etebarmelicod,
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