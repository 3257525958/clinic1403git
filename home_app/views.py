from django.shortcuts import render
from cantact_app.models import accuntmodel
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.
profilestatus =['']
loglevel = ['']
def home(request):
    if request.user.is_authenticated:
        us = accuntmodel.objects.all()
        for u in us:
            if u.melicode == request.user.username:
                profilestatus[0] = f"{u.firstname} {u.lastname} عزیز خوش آمدید "
                loglevel[0] = u.level
                break;
            else:
                profilestatus[0] = 'ورود به کاربری'
    else:
        profilestatus[0] = 'ورود به کاربری'

    return render(request,'home.html',context={ 'loglevel':loglevel[0],
                                                'profilestatus':profilestatus[0],
    })

def logute(request):
    logout(request)
    return redirect('/')
