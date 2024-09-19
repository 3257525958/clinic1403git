from django.shortcuts import render ,redirect
from it_app.models import mesaagetextmodel,mesaagemodel, homeimgmodel,homemobilemodel,homemenosarimodel
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
from cantact_app.views import strb,strd , stra,stry
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
                            except APIException as e:
                                m = 'tellerror'
                            except HTTPException as e:
                                m = 'neterror'
    return render(request,'mesage_send.html')
def tiketdef(request):
    selectmessage = request.POST.get('selectmessage')
    ms = mesaagemodel.objects.all()
    namesender =''
    textms=''

    if (selectmessage != None) and (selectmessage != '') and (selectmessage != 'None'):
        for n in ms:
            if n.id == selectmessage:
                m = mesaagemodel.objects.filter(id=n.id)
                m.update(idtiket=n.id,vaziyat='پاسخ داده شده')
                textms = n.textmessage
                users = accuntmodel.objects.all()
                for user in users:
                    if int(user.melicode) == int(n.melicod):
                        namesender = user.firstname + ' '+ user.lastname
        return render(request, 'tiket.html', context={
            'recivemessage': textms,
            'namesender': namesender,
        })

    listmessage = ['']
    listmessage.clear()
    for m in ms :
        if m.vaziyat == "در انتظار پاسخ":
            users = accuntmodel.objects.all()
            for user in users:
                if int(user.melicode) == int(m.melicod):
                    name = user.firstname + ' '+ user.lastname

                    listmessage.append((str(m.id) + "," +name).split(","))
    return render(request,'tiket.html',context={
        # 'listnonread':listmessage,
    })

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


def tim(x):
    if x == '1' :
        def tavalod_tabrik():
            print("mmmmmmmmmmmmmmmmm")
            users = accuntmodel.objects.all()
            t = datetime.datetime.now()
            for user in users:
                if (user.mountb == strb(t)) and (user.dayb == strd(t)):
                    name = user.firstname + ' ' + user.lastname
                    smstext = 'سلام' + ' ' + name + ' ' + 'عزیز' + '\n' + "زادروز تولدتان مبارک"+'\n'+'مفتخریم تا با هدیه ای هر چند کوچک در این مناسبت فرخنده در کنار شما باشیم'+'\n'+'برای دریافت هدیه عدد 3 را به همین سامانه ارسال فرمایید'+'\n'+'مطب دکتر اسدپور'+'\n'+'لغو 11'
                    try:
                        api = KavenegarAPI(
                            '527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D')
                        params = {
                            'sender': '9982003178',  # optional
                            'receptor': user.phonnumber,  # multiple mobile number, split by comma
                            'message': smstext,
                        }
                        response = api.sms_send(params)
                        # return render(request, 'code_cantact.html')
                    except APIException as e:
                        m = 'tellerror'
                    except HTTPException as e:
                        m = 'neterror'

        # Schedule the message to be sent at midnight
        schedule.every().day.at("00:00").do(tavalod_tabrik)
        # schedule.every(5).seconds.do(tavalod_tabrik)
        while True:
            schedule.run_pending()
            time.sleep(1)
    if x == '2' :
        def yadavari_vaghtfarda():
            print("ddddddddfffffffffttttttttttttttttt")
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
                            except HTTPException as e:
                                m = 'neterror'
        # Schedule the message to be sent at midnight
        schedule.every().day.at("08:30").do(yadavari_vaghtfarda)
        # schedule.every(20).seconds.do(yadavari_vaghtfarda)
        while True:
            schedule.run_pending()
            time.sleep(1)
    if x == '3':
        def savemesaage():
            print("ooooooooooooooooooooooooooooooooooooo")
            res = requests.post("https://api.kavenegar.com/v1/527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D/sms/receive.json?linenumber=9982003178&isread=0")
            r = res.json()
            a = ['']
            a.clear()
            if r["entries"] != []:
                for i in range(len(r["entries"])):
                    ba = ['']
                    ba.clear()
                    ba.append(str(r["entries"][i]['message']))
                    ba.append(str(r["entries"][i]["sender"]))
                    ba.append((str(r["entries"][i]["date"])))
                    a.append(ba)
                t = datetime.datetime.now()
                t += timedelta(days=1)
                for aaa in a :
                    if aaa[0] == "1" :
                        print("qqqqqqqqqqqqqqqqqqqqqqqqqqq")
                        users = accuntmodel.objects.all()
                        for user in users:
                            if user.phonnumber == aaa[1] :
                                rs = reservemodel.objects.all()
                                for r in rs:
                                    if (r.datemiladireserv == t.strftime('%a %d %b %y')) and (r.melicod == user.melicode):
                                        re =reservemodel.objects.filter(datemiladireserv=t.strftime('%a %d %b %y'),melicod=user.melicode)
                                        re.update(vaziyatereserv='قطعی')
                                        name = user.firstname + ' ' + user.lastname
                                        smstext =name + ' ' + 'عزیز' + '\n' + 'رزرو شما قطعی شد'+ '\n' +'با تشکر'+ 'مطب دکتر اسدپور' + '\n' + '\n' + '\n' + 'لغو ارسال پیامک 11'
                                        try:
                                            api = KavenegarAPI(
                                                '527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D')
                                            params = {
                                                'sender': '9982003178',  # optional
                                                'receptor': user.phonnumber,  # multiple mobile number, split by comma
                                                'message': smstext,
                                            }
                                            response = api.sms_send(params)
                                        except APIException as e:
                                            m = 'tellerror'
                                        except HTTPException as e:
                                            m = 'neterror'
                    if aaa[0] == "2" :
                        print("hhhhhhhhhhhhhhhhhhhh")
                        users = accuntmodel.objects.all()
                        for user in users:
                            if user.phonnumber == aaa[1] :
                                rs = reservemodel.objects.all()
                                for r in rs:
                                    if (r.datemiladireserv == t.strftime('%a %d %b %y')) and (r.melicod == user.melicode):
                                        re =reservemodel.objects.filter(datemiladireserv=t.strftime('%a %d %b %y'),melicod=user.melicode)
                                        re.update(vaziyatereserv='کنسل')
                                        name = user.firstname + ' ' + user.lastname
                                        smstext =name + ' ' + 'عزیز' + '\n' + 'رزرو شما کنسل شد همکاران برای هماهنگی با شما تماس خواهند گرفت'+ '\n' +'با تشکر'+ 'مطب دکتر اسدپور' + '\n' + '\n' + '\n' + 'لغو ارسال پیامک 11'
                                        try:
                                            api = KavenegarAPI(
                                                '527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D')
                                            params = {
                                                'sender': '9982003178',  # optional
                                                'receptor': user.phonnumber,  # multiple mobile number, split by comma
                                                'message': smstext,
                                            }
                                            response = api.sms_send(params)
                                        except APIException as e:
                                            m = 'tellerror'
                                        except HTTPException as e:
                                            m = 'neterror'
                    if (aaa[0] != "2") and (aaa[0] != "1") and (aaa[0] != "11"):
                        print("zzzzzzzzzzzzzzzzzz")
                        users = accuntmodel.objects.all()
                        for user in users:
                            if user.phonnumber == aaa[1] :
                                t = datetime.datetime.now()
                                mesaagemodel.objects.create(
                                    melicod=user.melicode,
                                    dateyear =stry(t),
                                    datemuonth =strb(t),
                                    dateday =stra(t),
                                    phonnumber =user.phonnumber,
                                    textmessage = aaa[0],
                                )

        schedule.every(10).seconds.do(savemesaage)
        while True:
            schedule.run_pending()
            time.sleep(1)
t1 = Thread(target=tim,args="1")
t2 = Thread(target=tim,args="2")
t3 = Thread(target=tim,args="3")
# t1.start()
# t2.start()
# t3.start()
