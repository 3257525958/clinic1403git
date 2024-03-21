from django.contrib.auth import authenticate, login
from django.shortcuts import render , redirect
from django.views import View
import requests
from django.conf import settings
import requests
import json
from django.http import HttpResponse
from kavenegar import KavenegarAPI, APIException, HTTPException
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User

from reserv_app.models import reservemodeltest,reservemodel,neursemodel,neursetestmodel
from cantact_app.models import accuntmodel



class OrderPageView(View):
    def get(self, request):
        return render(request,'reserv_end.html')



amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/zib/verify/'
merchandzibal = "zibal"
#? sandbox merchant
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'
ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

class OrderPayView(View):
    def get(self,request):
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": amount,
            "Description": description,
            "Phone": phone,
            "CallbackURL": CallbackURL,
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        res = requests.post(ZP_API_REQUEST, data=data,headers=headers)
        if res.status_code == 200 :
            response = res.json()
            if response['Status'] == 100 :
                url = f"{ZP_API_STARTPAY}{response['Authority']}"
                return redirect(url)
        else:
            print(res.json()['errors'])
            return HttpResponse(str(res.json()['errors']))
class VerifyPayView(View):
    def get(self,request):
        authority = request.GET['Authority']
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": amount,
            "Authority" : authority,
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        res = requests.post(ZP_API_VERIFY, data=data,headers=headers)
        if res.status_code == 200 :
            response = res.json()
            if response['Status'] == 100 :
                return HttpResponse({'Status': response['Status'],'RefID':response['RefID']})
            else:
                return HttpResponse({'Status': response['Status'],'RefID':response['RefID']})
        else:
            return HttpResponse('پرداخت ناموفق')






# Irandargah_request_url = f"https://dargaah.com/payment"
# merchand_irandargah='69097262-cc95-4999-9d6c-2fe5865bb891'
# Irandargah_send_url="https://dargaah.com/ird/startpay/"
# Irandargah_verify_url='https://dargaah.com/verification'
Irandargah_request_url = f"https://dargaah.com/sandbox/payment"
merchand_irandargah='TEST'
Irandargah_send_url="https://dargaah.com/sandbox/ird/startpay/"
Irandargah_verify_url="https://dargaah.com/sandbox/verification"
# callbackirandargaah = 'http://drmahdiasadpour.ir/zib/irandargahcallback/'
callbackirandargaah = 'http://127.0.0.1:8000/zib/irandargahcallback/'
class OrderPayViewirandagaah(View):
    def get(self,request):
        data = {
            'merchantID': merchand_irandargah,
            'amount': 10000,  # amount of transaction in rial (amount must be between 10,000 and 500,000,000 rial)
            'callbackURL': callbackirandargaah,
            'orderId': '1234',  # you can set your desired unique order id for transaction
            'mobile': '09122852099',  # for more information in transaction's detail // OPTIONAL
            'description': 'YOUR DESCRIPTION'  # for more information in transaction's detail // OPTIONAL
        }
        data = json.dumps(data)
        url = Irandargah_request_url
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        res = requests.post(url, data=data,headers=headers)
        if res.status_code == 200 :
            response = res.json()
            urll = f"{Irandargah_send_url}{response['authority']}"
            return redirect(urll)
        else:
            return HttpResponse(str(res.json()['message']))
# ++++++++++++++++\
class Verifyi(View):
    def get(self,request):
        if request.POST['code'] == 100:
            data = {
                'merchantID': merchand_irandargah,
                'authority': request.POST['authority'],
                'amount': int(request.POST['amount']),
                'orderId': request.POST['orderId'],
            }
            data = json.dumps(data)
            url = Irandargah_request_url
            headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
            res = requests.post(url, data=data, headers=headers)
            if res.status_code == 200 :
                response = res.json()
                if response['Status'] == 100 :
                    return HttpResponse({'Status': response['Status'],'RefID':response['RefID']})
                else:
                    return HttpResponse({'Status': response['Status'],'RefID':response['RefID']})
            else:
                return HttpResponse('پرداخت ناموفق')

        else:
            print('error in transaction\'s payment: ' + request.POST['message'])
            return render(request, 'test.html')




ZIB_API_REQUEST = "https://gateway.zibal.ir/v1/request"
ZIB_API_VERIFY = "https://gateway.zibal.ir/verify"
ZIB_API_STARTPAY = "https://gateway.zibal.ir/start/"
# callbackzibalurl = 'http://127.0.0.1:8000/zib/verifyzibal/'
merchanzibal = 'zibal'
callbackzibalurl = 'https://drmahdiasadpour.ir/zib/verifyzibal/'
# merchanzibal = '64c2047fcbbc270017f4c6b2'
m=["0"]
peyment = 50000
phonnumber = ["0"]
def orderzibal(request):
    if request.user.is_authenticated:
        users = accuntmodel.objects.all()
        for user in users:
            if user.melicode == request.user.username:
                phonnumber[0] = user.phonnumber
                m[0] = user.melicode
    data = {
        "merchant": merchanzibal,
        "amount": peyment,
        "callbackUrl": callbackzibalurl,
        "description": "بیعانه جهت رزرو",
        "orderId": "ZBL-7799",
        "mobile": str(phonnumber[0])
    }
    data = json.dumps(data)
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    res = requests.post(ZIB_API_REQUEST, data=data, headers=headers)
    r = res.json()
    if res.status_code == 200:
        if r['result'] == 100:
            url = f"{ZIB_API_STARTPAY}{r['trackId']}"

            return redirect(url)
    else:
        return HttpResponse(str(res.json()['errors']))

    def get(self,request):
        authority = request.GET['Authority']
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": amount,
            "Authority" : authority,
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        res = requests.post(ZP_API_VERIFY, data=data,headers=headers)
        if res.status_code == 200 :
            response = res.json()
            if response['Status'] == 100 :
                return HttpResponse({'Status': response['Status'],'RefID':response['RefID']})
            else:
                return HttpResponse({'Status': response['Status'],'RefID':response['RefID']})
        else:
            return HttpResponse('پرداخت ناموفق')
endresult = ["t"]
endresult.clear()

def callbackzibal(request):
    endresult.clear()
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
        endresult.append(r['message'])
        endresult.append(r['cardNumber'])
        endresult.append(trac)
        users = accuntmodel.objects.all()
        for user in users:
            if user.melicode == m[0]:
                phonnumber[0] = user.phonnumber
                endresult.append(user.melicode)
                endresult.append(str(user.phonnumber))
                endresult.append(user.firstname)
                endresult.append(user.lastname)
    if endresult[0] == "success":
        reserve = reservemodeltest.objects.all()
        for r in reserve :
            if r.mellicode == m[0]:
                endresult.append(r.jobreserv+" "+r.detalereserv)
                endresult.append(r.dateshamsireserv)
                endresult.append(r.hourreserv)
                reservemodel.objects.create(melicod =str(request.user.username),
                                            jobreserv=r.jobreserv,
                                            detalereserv=r.detalereserv,
                                            personreserv=r.personreserv,
                                            timereserv=r.timereserv,
                                            castreserv=r.castreserv,
                                            numbertime=r.numbertime,
                                            hourreserv=r.hourreserv,
                                            dateshamsireserv=r.dateshamsireserv,
                                            datemiladireserv=r.datemiladireserv,
                                            yearshamsi=r.yearshamsi,
                                            cardnumber="result[1]",
                                            pyment=peyment,
                                            trakingcod = str(endresult[2]),
                                            bank= "zibal"
                                            )
                a = reservemodeltest.objects.filter(mellicode=m[0])
                a.delete()
        neurse = neursetestmodel.objects.all()
        for r in neurse :
            if r.mellicode == m[0]:
                neursemodel.objects.create(
                    mellicode=m[0],
                    inject_botax=r.inject_botax,
                    illnes=r.illnes,
                    drug=r.drug,
                    sensivety=r.sensivety,
                    pregnancy=r.pregnancy,
                    date_finaly=r.date_finaly,
                    image_show=r.image_show,
                    satisfact=r.satisfact,
                )
                a = neursetestmodel.objects.filter(mellicode=m[0])
                a.delete()

    # return redirect('http://127.0.0.1:8000/zib/end/')
    return redirect('https://drmahdiasadpour.ir/zib/end/')

def end(request):
    # print(result[0])
    # print(result[1])
    # print(result[2])
    # print(result[3])
    # print(result[4])
    # print(result[5])
    # print(result[6])
    print(endresult)
    print(request)
    logout(request)

    backbutton = request.GET.get("backbutton")
    if backbutton == "accept":
        us = User.objects.all()
        for u in us :
            print(u.username,endresult[3])
            if str(u.username) == str(endresult[3]):
                user_login = authenticate(request,
                                          username=u.username,
                                          password=u.password,
                                          )
                print("okokokokokokokokokokok")
                if user_login is not None:
                    print("مممممممممممممممممممممممممممممم")
                    login(request, user_login)
                return render(request,"home.html",context={'u':u.username,
                                                           'p':u.password,
                                                           })
                # return redirect('https://drmahdiasadpour.ir/')
    message = f"{endresult[5]}_{endresult[6]}پرداخت_موفقیت_آمیز_کدرهگیری_{endresult[2]}دکتر_اسدپور_"

    try:
        api = KavenegarAPI(
            '527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D')
        params = {
            'receptor': endresult[4],
            'template': 'test',
            'token': message,
            'type': 'sms',
        }
        response = api.verify_lookup(params)
        return render(request, 'end.html', context={"result": endresult, })
    except APIException as e:
        m = 'tellerror'
        # messages.error(request,'در سیستم ارسال پیامک مشکلی پیش آمده لطفا شماره خود را به درستی وارد کنید و دوباره امتحان کنید در صورتی که مشکل برطرف نشد در اینستاگرام پیام دهید ')
        return render(request, 'end.html', context={"result": endresult, })
    except HTTPException as e:
        m = 'neterror'
        # messages.error(request,'در سیستم ارسال پیامک مشکلی پیش آمده لطفا شماره خود را به درستی وارد کنید و دوباره امتحان کنید در صورتی که مشکل برطرف نشد در اینستاگرام پیام دهید ')
        # return render(request, 'add_cantact.html')
        return render(request, 'end.html', context={"result": endresult, })
