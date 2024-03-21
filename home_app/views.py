from django.shortcuts import render
from cantact_app.models import accuntmodel
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.
profilestatus =['']
loglevel = ['']
def home(request):
    print("ooooooooooooooooooooooooooooooooojjjjjjjjjjjjjjjjjjjjjjjjjjjjjmmmmmmmmmmmmmmm",request.user.username)
    print("1",request.headers)
    print("2",request.body)
    print("3",request.content_params)
    print("4",request.method)
    print("5",request.path)
    print("6",request.META)
    if request.user.is_authenticated:
        us = accuntmodel.objects.all()
        for u in us:
            if u.melicode == request.user.username:
                print("llllllllllllllllllllllllllll",request)
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
    print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr",request)

    return redirect('/')
