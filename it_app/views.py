from django.shortcuts import render
from it_app.models import mesaagetextmodel,mesaagecuntermodel, homeimgmodel,homemobilemodel,homemenosarimodel
import datetime
from cantact_app.views import stry,strd,strb,stra
from it_app.form import homeimgform,homemenosariform,homemobileform
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


def itcontrol(request):
    savebottom = request.POST.get("savebottom")
    select = request.POST.get("select")
    etebarit = "None"
    form = homeimgform(request.POST, request.FILES)

    if select == "منوی سریع" :
        form = homemenosariform(request.POST, request.FILES)
    if select == "عکس صفحه اصلی موبایل" :
        form = homemobileform(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        etebarit = "true"
    if savebottom == "accept" :
        return render(request,'it_control.html',context={
                                                                        'form':form,
                                                                        'etebarit':etebarit,
                                                                        })
    return render(request,'it_control.html',context={
                                                                    'form':form,
                                                                    'etebarit':etebarit,
                                                                    })


def itdeletcontrol(request):
    selectdelet =request.POST.get("selectdelet")
    if selectdelet == None :
        selectdelet = "انتخاب کنید"
    selectjlist =request.POST.get("selectjlist")
    if selectjlist == None :
        selectjlist = "انتخاب کنید"
    savebottom =request.POST.get("savebottom")
    etebarit = "false"
    jlist = ['']
    jlist.clear()


    if selectdelet =="عکس صفحه اصلی کامپیوتر" :
        os = homeimgmodel.objects.all()
        for o in os:
            jlist.append(o)
    if selectdelet =="عکس صفحه اصلی موبایل" :
        os = homemobilemodel.objects.all()
        for o in os:
            jlist.append(o)
    if selectdelet =="منوی سریع" :
        os = homemenosarimodel.objects.all()
        for o in os:
            jlist.append(o)

    if savebottom == "accept":
        if selectdelet == "عکس صفحه اصلی کامپیوتر":
            a = homeimgmodel.objects.filter(name=selectjlist)
            a.delete()
            etebarit = "true"
        if selectdelet == "عکس صفحه اصلی موبایل":
            a = homemobilemodel.objects.filter(name=selectjlist)
            a.delete()
            etebarit = "true"
        if selectdelet == "منوی سریع":
            a = homemenosarimodel.objects.filter(name=selectjlist)
            a.delete()
            etebarit = "true"
    return render(request,'it-deletcontrol.html', context={
                                                                        'jlist':jlist,
                                                                        'selectdelet':selectdelet,
                                                                        'selectj':selectjlist,
                                                                        'etebarit':etebarit,
                                                                        })