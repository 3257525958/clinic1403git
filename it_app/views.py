from django.shortcuts import render
from it_app.models import mesaagetextmodel,mesaagecuntermodel, homeimgmodel,homemobilemodel,homemenosarimodel
import datetime
from cantact_app.views import stry,strd,strb,stra
from it_app.form import homeimgform,homemenosariform,homemobileform
import datetime
from datetime import timedelta
from kavenegar import *
from reserv_app.models import reservemodel
from cantact_app.models import accuntmodel
import schedule
import time
import requests
from multiprocessing import process
from threading import Thread
from cantact_app.views import strb,strd
def sendmesaage(request):
    sendmethod =request.POST.get('sendmethod')
    sendsms = request.POST.get('sendsms')
    smstext = ''
    if sendsms == "accept" :
        if sendmethod == "1" :
            t = datetime.datetime.now()
            t += timedelta(days=1)
            rs = reservemodel.objects.all()
            for r in rs:
                if t.strftime('%a %d %b %y') == r.datemiladireserv :
                    users = accuntmodel.objects.all()
                    for user in users:
                        if int(user.melicode) == int(r.melicod) :
                            name = user.firstname + ' '+ user.lastname
                            smstext = 'سلام'+' '+name+' '+'عزیز'+'\n'+'شما فردا'+' '+r.dateshamsireserv+' '+'ساعت'+' '+r.hourreserv+' '+'برای'+' '+r.jobreserv+' '+r.detalereserv+' '+'وقت رزرو شده دارید'+' '+' برای تایید عدد 1 و برای لغو وقتتان عدد 2 را به همین سامانه پیامک نمایید همچنین برای تغییر وقت یا موارد دیگر میتوانید در همین سامانه پیام دهید'+'\n'+'مطب دکتر اسدپور'+'\n'+'\n'+'\n'+'لغو ارسال پیامک 11'
                            try:
                                api = KavenegarAPI(
                                    '527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D')
                                params = {
                                    'sender': '9982003178',  # optional
                                    'receptor': user.phonnumber,  # multiple mobile number, split by comma
                                    'message':smstext,
                                }
                                response = api.sms_send(params)
                                # return render(request, 'code_cantact.html')
                            except APIException as e:
                                m = 'tellerror'
                                return render(request, 'closecash.html', context={'melicod_etebar': m})
                            except HTTPException as e:
                                m = 'neterror'
                                return render(request, 'closecash.html', context={'melicod_etebar': m}, )

    return render(request,'mesage_send.html')
def savemesaage(request):
    savebutton = request.POST.get('savebutton')
    mesaagename = request.POST.get('mesaagename')
    mesaagetext = request.POST.get('mesaagetext')
    res = requests.post("https://api.kavenegar.com/v1/527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D/sms/receive.json?linenumber=9982003178&isread=0")
    r = res.json()
    a = ['']
    a.clear()
    for i in range(len(r["entries"])):
        a.append(str(r["entries"][i]['message']))
        a.append(str(r["entries"][i]["sender"]))


    # if (savebutton == 'accept') and (mesaagename != '') and (mesaagetext != '') and (mesaagename != None) and (mesaagetext != None):
    #     t = datetime.datetime.now()
    #     p = request.user.username
    #     mesaagetextmodel.objects.create(name=mesaagename,dateyear=stry(t),datemuonth=strb(t),dateday=strd(t),dateweek=stra(t),sender=p)
    return render(request,'mesaage_save.html',context={'a':a})


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


def tim():
    def sen():
        users = accuntmodel.objects.all()
        t = datetime.datetime.now()
        for user in users:
            if (user.mountb == strb(t)) and (user.dayb == strd(t)):
                name = user.firstname + ' ' + user.lastname
                smstext = 'سلام' + ' ' + name + ' ' + 'عزیز' + '\n' + "تولدت مبارک"+'\n'+'\n'+'\n'+'لغو 11'
                try:
                    api = KavenegarAPI(
                        '527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D')
                    params = {
                        'sender': '9982003178',  # optional
                        'receptor': "09122852099",  # multiple mobile number, split by comma
                        'message': smstext,
                    }
                    response = api.sms_send(params)
                    # return render(request, 'code_cantact.html')
                except APIException as e:
                    m = 'tellerror'
                except HTTPException as e:
                    m = 'neterror'

    # Schedule the message to be sent at midnight
    schedule.every().day.at("03:00").do(sen)
    while True:
        schedule.run_pending()
        time.sleep(1)


t = Thread(target=tim)
t.start()
print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print(datetime.datetime.now())