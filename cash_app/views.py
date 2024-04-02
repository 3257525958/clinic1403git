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

from reserv_app.models import reservemodeltest,reservemodel,neursemodel,filepage1model
from cantact_app.models import accuntmodel

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
