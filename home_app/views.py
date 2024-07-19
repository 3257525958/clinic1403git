from django.shortcuts import render
from cantact_app.models import accuntmodel
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from reserv_app.models import reservemodeltest,reservemodel,neursemodel,filepage1model
from jobs_app.models import workmodel
from it_app.models import homeimgmodel,homemenosarimodel,homemobilemodel


# Create your views here.
profilestatus =['']
loglevel = ['']
def home(request):
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
