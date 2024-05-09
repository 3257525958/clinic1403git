from django.shortcuts import render
from it_app.models import mesaagetextmodel,mesaagecuntermodel
import datetime
from cantact_app.views import stry,strd,strb,stra
def sendmesaage(request):
    return render(request,'mesage_send.html')
def savemesaage(request):
    savebutton = request.POST.get('savebutton')
    mesaagename = request.POST.get('mesaagename')
    mesaagetext = request.POST.get('mesaagetext')
    if (savebutton == 'accept') and (mesaagename != '') and (mesaagetext != '') and (mesaagename != None) and (mesaagetext != None):
        t = datetime.datetime.now()
        p = request.user.username
        mesaagetextmodel.objects.create(name=mesaagename,dateyear=stry(t),datemuonth=strb(t),dateday=strd(t),dateweek=stra(t),sender=p)
    return render(request,'mesaage_save.html')
