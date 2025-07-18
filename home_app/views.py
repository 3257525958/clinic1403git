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



# if 1==1 :
#     if 1 == 1 :
#         if 1==1 :
#             ms = mesaagemodel.objects.all()
#             users = accuntmodel.objects.all()
#             try:
#                 for user in users:
#                     nayme = 'false'
#                     maede = 'false'
#                     nilofal = 'false'
#                     sara = 'false'
#                     print(user.melicode)
#                     for m in ms :
#                         if ('2259640788' == str(m.sendermelicod)) or ('2259640788' == str(user.melicode)):
#                             nayme = 'true'
#                         print(nayme)
#                         if ('1050301811' == str(m.sendermelicod)) or ('1050301811' == str(user.melicode)):
#                             maede = 'true'
#                         print(maede)
#                         if ('1741694000' == str(m.sendermelicod)) or ('1741694000' == str(user.melicode)):
#                             nilofal = 'true'
#                         print(nilofal)
#                         if ('0019909306' == str(m.sendermelicod)) or ('0019909306' == str(user.melicode)):
#                             sara = 'true'
#                         print(sara)
#                     if len(user.melicode) == 10:
#                         if nayme == "false":
#                             mesaagemodel.objects.create(
#                                         recivermelicod=str(user.melicode),
#                                         vaziyat="در انتظار پاسخ",
#                                         sendermelicod='2259640788',
#                                         textmessage='سلام من در مطب دکتر اسدپور مشاور پزشکی و مدیر هستم ، خوشال میشم بتونم کمکتون کنم ',
#
#                                     )
#                         if maede == "false":
#                             mesaagemodel.objects.create(
#                                         recivermelicod=str(user.melicode),
#                                         vaziyat="در انتظار پاسخ",
#                                         sendermelicod='1050301811',
#                                         textmessage='سلام من در مطب دکتر اسدپور مسئول اتاق فیشیال و تولید محتوا هستم ، خوشال میشم بتونم کمکتون کنم ',
#
#                                     )
#                         if sara == "false":
#                             mesaagemodel.objects.create(
#                                         recivermelicod=str(user.melicode),
#                                         vaziyat="در انتظار پاسخ",
#                                         sendermelicod='0019909306',
#                                         textmessage='سلام من در مطب دکتر اسدپور مسئول رزروشن  و مدیر داخلی هستم ، خوشال میشم بتونم کمکتون کنم ',
#
#                                     )
#                         if nilofal == "false":
#                             mesaagemodel.objects.create(
#                                         recivermelicod=str(user.melicode),
#                                         vaziyat="در انتظار پاسخ",
#                                         sendermelicod='1741694000',
#                                         textmessage='سلام من در مطب دکتر اسدپور مسئول اتاق لیزر هستم ، خوشال میشم بتونم کمکتون کنم ',
#
#                                     )
#             except:
#                 print("net erro in home app")



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
    img = ''
    login_user = 'false'
    user_position = ''
    if request.user.is_authenticated:
        login_user = 'true'
        us = accuntmodel.objects.all()
        for u in us:
            if u.melicode == request.user.username:
                profilestatus[0] = f"{u.firstname} {u.lastname}  "
                user_position = u.level
                if u.profile_picture and hasattr(u.profile_picture, 'url'):
                    img = u.profile_picture.url
                else:
                    img = '/static/img/login.jpg'
                #     # مسیر به تصویر پیش‌فرض در پوشه static
                # img = u.profile_picture
                loglevel[0] = u.level
                user_profile = u
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
    b = request.POST.get('pagesize')
    d = 0
    if b != None :
        d = int(b)
    return render(request,'new_home.html',context={
                                                                'loglevel':loglevel[0],
                                                                'profilestatus': profilestatus[0],
                                                                'user_position':user_position,
                                                                'img':img,
                                                                'login_user':login_user,
                                                                })

def logute(request):
    logout(request)
    return redirect('/')


