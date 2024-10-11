from django.shortcuts import render
from cantact_app.models import accuntmodel
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from reserv_app.models import reservemodeltest,reservemodel,neursemodel,filepage1model
from jobs_app.models import workmodel
from it_app.models import *
from kavenegar import *
import schedule
import time
from threading import Thread


# Create your views here.
# for m in mesaagemodel.objects.all() :
#     a= mesaagemodel.objects.filter(id=m.id)
#     a.delete()

print("qqqqqqqq")
if 1==1 :
    print("gggggggggg")
    if 1 == 1 :

        if 1==1 :
            ms = mesaagemodel.objects.all()
            users = accuntmodel.objects.all()
            try:
                for user in users:
                    nayme = 'false'
                    maede = 'false'
                    nilofal = 'false'
                    sara = 'false'
                    print(user.melicode)
                    for m in ms :
                        if ('2259640788' == str(m.sendermelicod)) or ('2259640788' == str(user.melicode)):
                            nayme = 'true'
                        print(nayme)
                        if ('1050301811' == str(m.sendermelicod)) or ('1050301811' == str(user.melicode)):
                            maede = 'true'
                        print(maede)
                        if ('1741694000' == str(m.sendermelicod)) or ('1741694000' == str(user.melicode)):
                            nilofal = 'true'
                        print(nilofal)
                        if ('0019909306' == str(m.sendermelicod)) or ('0019909306' == str(user.melicode)):
                            sara = 'true'
                        print(sara)
                    if len(user.melicode) == 10:
                        if nayme == "false":
                            mesaagemodel.objects.create(
                                        recivermelicod=str(user.melicode),
                                        vaziyat="در انتظار پاسخ",
                                        sendermelicod='2259640788',
                                        textmessage='سلام من در مطب دکتر اسدپور مشاور پزشکی و مدیر هستم ، خوشال میشم بتونم کمکتون کنم ',

                                    )
                        if maede == "false":
                            mesaagemodel.objects.create(
                                        recivermelicod=str(user.melicode),
                                        vaziyat="در انتظار پاسخ",
                                        sendermelicod='1050301811',
                                        textmessage='سلام من در مطب دکتر اسدپور مسئول اتاق فیشیال و تولید محتوا هستم ، خوشال میشم بتونم کمکتون کنم ',

                                    )
                        if sara == "false":
                            mesaagemodel.objects.create(
                                        recivermelicod=str(user.melicode),
                                        vaziyat="در انتظار پاسخ",
                                        sendermelicod='0019909306',
                                        textmessage='سلام من در مطب دکتر اسدپور مسئول رزروشن  و مدیر داخلی هستم ، خوشال میشم بتونم کمکتون کنم ',

                                    )
                        if nilofal == "false":
                            mesaagemodel.objects.create(
                                        recivermelicod=str(user.melicode),
                                        vaziyat="در انتظار پاسخ",
                                        sendermelicod='1741694000',
                                        textmessage='سلام من در مطب دکتر اسدپور مسئول اتاق لیزر هستم ، خوشال میشم بتونم کمکتون کنم ',

                                    )
            except:
                print("net erro in home app")
#         schedule.every(30).seconds.do(cke)
#         while True:
#             schedule.run_pending()
#             time.sleep(1)
#
# t11 = Thread(target=st,args="1")
# t11.start()
#
profilestatus =['']

loglevel = ['']
def home(request):
    btndate = request.POST.get('btndate')
    # if btndate == 'accept':
    #     try:
    #         api = KavenegarAPI(
    #             '527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D')
    #         params = {
    #             'sender': '9982003178',  # optional
    #             'receptor': '09122852099',  # multiple mobile number, split by comma
    #             'message':" سلام",
    #         }
    #         response = api.sms_send(params)
    #         # return render(request, 'code_cantact.html')
    #     except APIException as e:
    #         m = 'tellerror'
    #         return render(request, 'closecash.html', context={'melicod_etebar': m})
    #     except HTTPException as e:
    #         m = 'neterror'
    #         return render(request, 'closecash.html', context={'melicod_etebar': m}, )

    r = request.GET.get("r")
    loglevel[0] = [""]
    profilestatus = ['']
    if (r !="") and (r != None):
        allreserv = reservemodel.objects.all()
        for oneobject in allreserv :
            if oneobject.trakingcod == r :
                allacant = accuntmodel.objects.all()
                for oneacant in allacant :
                    if oneacant.melicode == oneobject.melicod :
                        user_login = authenticate(request,
                                                  username=oneacant.melicode,
                                                  password=oneacant.pasword,
                                                  )
                        if user_login is not None:
                            login(request, user_login)
                            # return redirect('https://drmahdiasadpour.ir')
                            return redirect('http://127.0.0.1:8000')
    if request.user.is_authenticated:
        us = accuntmodel.objects.all()
        for u in us:
            if u.melicode == request.user.username:
                profilestatus[0] = f"{u.firstname} {u.lastname}  "
                loglevel[0] = u.level
                break;
            # else:
            #     profilestatus[0] = 'ورود به کاربری'
    # else:
    #     profilestatus[0] = 'ورود به کاربری'
    images = []
    us =homeimgmodel.objects.all()
    for u in us:
        images.append(u)
    imagesari = []
    us =homemenosarimodel.objects.all()
    for u in us:
        imagesari.append(u)
    imgmobile = []
    us =homemobilemodel.objects.all()
    for u in us:
        imgmobile.append(u)

    btsize = request.POST.get('btsize')
    b = request.POST.get('na')
    d = 0
    if b != None :
        d = int(b)
    return render(request,'home.html',context={ 'loglevel':loglevel[0],
                                                'profilestatus':profilestatus[0],
                                                'images':images,
                                                'imagesari':imagesari,
                                                'imgmobile':imgmobile,
                                                'bsize':d,
    })

def logute(request):
    logout(request)
    return redirect('/')


