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
    sel =request.POST.get("sel")
    if (sel == None) or (sel == '') or (sel == 'None'):
        sel = '0'
    selectjlist =request.POST.get("selectjlist")
    savebottom =request.POST.get("savebottom")
    etebarit = "false"
    jlist = ['']
    jlist.clear()
    p = ['']

    if int(sel) == 1 :
        os = homeimgmodel.objects.all()
        for o in os:
            s = (str(o.id) + "," + o.name).split(",")
            jlist.append(s)
        p = (sel + "," + "عکس صفحه اصلی کامپیوتر").split(",")

    if sel =="2" :
        os = homemobilemodel.objects.all()
        for o in os:
            s = (str(o.id) + "," + o.name).split(",")
            jlist.append(s)
        p = (sel + "," + "عکس صفحه اصلی موبایل").split(",")
    if sel =="3" :
        os = homemenosarimodel.objects.all()
        for o in os:
            s = (str(o.id) + "," + o.name).split(",")
            jlist.append(s)
        p = (sel + "," + "منوی سریع").split(",")

    if savebottom == "accept":
        if sel == "1":
            a = homeimgmodel.objects.filter(id=selectjlist)
            a.delete()
            etebarit = "true"
        if sel == "2":
            a = homemobilemodel.objects.filter(id=selectjlist)
            a.delete()
            etebarit = "true"
        if sel == "3":
            a = homemenosarimodel.objects.filter(id=selectjlist)
            a.delete()
            etebarit = "true"
    return render(request,'it-deletcontrol.html', context={
                                                                        'jlist':jlist,
                                                                        'selectj':selectjlist,
                                                                        'etebarit':etebarit,
                                                                        'p':p,
                                                                        })


