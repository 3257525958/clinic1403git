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
from home_app.views import *
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

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


def chatlistproduct(usercodemeli,melicodselet,masli):
    if melicodselet != '':
        ms = mesaagemodel.objects.all()
        chatlist = ['']
        chatlist.clear()
        f = '0'
        e = '0'
        for i in range(int(len(masli))):
            for m in ms:
                if int(m.id) == int(masli[i]):
                    messagerul = ''
                    if (int(m.recivermelicod) == int(usercodemeli)) and (
                            int(m.sendermelicod) == int(melicodselet)):
                        messagerul = 'reciver'
                    if (int(m.sendermelicod) == int(usercodemeli)) and (
                            int(m.recivermelicod) == int(melicodselet)):
                        messagerul = 'sender'
                    if messagerul != '':
                        a = mesaagemodel.objects.filter(id=m.id)
                        a.update(vaziyat="پاسخ داده شده")
                        if messagerul == 'reciver':
                            array = ['']
                            array.clear()
                            array.append(m.messagemethod)
                            array.append('0')
                            array.append(m.textmessage)
                            array.append(str(m.hour) + ':' + str(m.minute))
                            array.append(f)
                            chatlist.append(array)
                            f = '1'
                            e = '0'

                        if messagerul == 'sender':
                            array = ['']
                            array.clear()
                            array.append(m.messagemethod)
                            array.append('1')
                            array.append(m.textmessage)
                            array.append(str(m.hour) + ':' + str(m.minute))
                            array.append(e)
                            chatlist.append(array)
                            f = '0'
                            e = '1'
        chatlist.reverse()
        return (chatlist)


def tiketdef(request):
    try:
        check = request.POST.get('check')
        sendbtn = request.POST.get('sendbtn')
        textsend = request.POST.get('textsend')
        melicodanswer = request.POST.get('melicodanswer')
        unreadbtn = request.POST.get('unreadbtn')
        readbtn = request.POST.get('readbtn')

        textmes = ''
        if check == 'accept':
            textmes = textsend
        if (melicodanswer != None) and (melicodanswer != ''):
            melicodselet = melicodanswer
        else:
            melicodselet =''
        # ---وقتی پیامی در فضای مجازی پیام بدهیم اینجا با این کد ملی ثبت نام میشه----
        if (melicodanswer == None) or (melicodanswer == '') or ( melicodanswer == "None"):
            # melicodanswer = '0'
            melicodanswer = request.user.username
        if (sendbtn != None) and (sendbtn != '') and (sendbtn != 'None')and (textsend != None) and (textsend != '') and (textsend != 'None') :
            t = datetime.datetime.now()
            mesaagemodel.objects.create(
                recivermelicod=sendbtn,
                vaziyat="در انتظار پاسخ",
                dateyear = stry(t),
                datemuonth = strb(t),
                dateday = stra(t),
                dateweek = strd(t),
                hour = t.strftime('%H'),
                minute = t.strftime('%M'),
                messagemethod = "مجازی",
                sendermelicod = request.user.username,
                textmessage = textsend,

            )

        notphonnamberarray = ['']
        notphonnamberarray.clear()
        ansphonnamberarray = ['']
        ansphonnamberarray.clear()

        # --مرتب کردن پیامها به ترتیب ثبت----
        ms = mesaagemodel.objects.all()
        m1 = ['']
        m1.clear()
        masli = ['']
        masli.clear()
        for m2 in ms :
            m1.append(m2.id)
            masli.append(0)
        m5 = m1
        for m3 in m1 :
            x = 0
            for m4 in m5:
                if m3 < m4 :
                    x+=1
            masli[x] = m3
        # در این ارایه ها درست میشن دز این ارایه ها بر اساس زمان از آخر به اول کد ملی ها ردف میشه -------------------ساخت ارایه پیامهای جدید
        for i in range(int(len(masli))):
            for mesaage in ms:
                if int(mesaage.id) == int(masli[i]) :
                    if mesaage.vaziyat == "در انتظار پاسخ":
                         if int(mesaage.recivermelicod) == int(request.user.username):
                            notphonnamberarray.append(mesaage.sendermelicod)
        # -----------------------------------------------------ساخت ارایه پیامهای قدیم--
        for i in range(int(len(masli))):
            for mesaage in ms:
                if int(mesaage.id) == int(masli[i]) :
                    rul = 'true'
                    if (int(mesaage.recivermelicod) != int(request.user.username)) and (int(mesaage.sendermelicod) != int(request.user.username)):
                        rul = 'false'
                    if (mesaage.vaziyat == "پاسخ داده شده") and (rul == 'true') :
                        b = 0
                        for r in notphonnamberarray:
                            if r == mesaage.sendermelicod :
                                b = 1
                        a = 0
                        for namber in ansphonnamberarray:
                            if namber == mesaage.sendermelicod:
                                a = 1
                        if (a == 0) and (b == 0) and (mesaage.sendermelicod != request.user.username):
                            ansphonnamberarray.append(mesaage.sendermelicod)
    # ------------------------

        # if melicodanswer == "0":
        if (unreadbtn != None) and (unreadbtn != '') and (unreadbtn != 'None') :
            melicodselet = notphonnamberarray[int(unreadbtn)]
        if (readbtn != None) and (readbtn != '') and (readbtn != 'None') :
            melicodselet = ansphonnamberarray[int(readbtn)]

        if melicodselet != '':
            name =''
            users = accuntmodel.objects.all()
            for user in users :
                if int(user.melicode) == int(melicodselet) :
                    name = user.firstname + ' ' + user.lastname

        #     ms = mesaagemodel.objects.all()
        #     chatlist = ['']
        #     chatlist.clear()
        #     f = '0'
        #     e = '0'
        #
        #     for i in range(int(len(masli))):
        #         for m in ms :
        #             if int(m.id) == int(masli[i]) :
        #                 messagerul = ''
        #                 if (int(m.recivermelicod) == int(request.user.username)) and (int(m.sendermelicod) == int(melicodselet)) :
        #                     messagerul = 'reciver'
        #                 if (int(m.sendermelicod) == int(request.user.username)) and (int(m.recivermelicod) == int(melicodselet)) :
        #                     messagerul = 'sender'
        #                 if messagerul != '':
        #                     a = mesaagemodel.objects.filter(id=m.id)
        #                     a.update(vaziyat="پاسخ داده شده")
        #                     if messagerul == 'reciver':
        #                         array = ['']
        #                         array.clear()
        #                         array.append(m.messagemethod)
        #                         array.append('0')
        #                         array.append(m.textmessage)
        #                         array.append(str(m.hour) + ':' + str(m.minute))
        #                         array.append(f)
        #                         chatlist.append(array)
        #                         f = '1'
        #                         e = '0'
        #
        #                     if messagerul == 'sender' :
        #                         array = ['']
        #                         array.clear()
        #                         array.append(m.messagemethod)
        #                         array.append('1')
        #                         array.append(m.textmessage)
        #                         array.append(str(m.hour) + ':' + str(m.minute))
        #                         array.append(e)
        #                         chatlist.append(array)
        #                         f = '0'
        #                         e = '1'
        #     chatlist.reverse()
            return render(request,'chatbox.html',context={
                'melicode':melicodselet,
                'name':name,
                'chatlist':chatlistproduct(request.user.username,melicodselet,masli),
                'textmes': textmes,
            })



        nananswer = ['']
        nananswer.clear()
        answer =['']
        answer.clear()
     # -------ارایه کامل پیامهای جدید----
        ms = mesaagemodel.objects.all()
        for meli in notphonnamberarray :
            name = ''
            messagenamber = 0
            mestext = ''
            date = ''
            meliarray = ['']
            meliarray.clear()
            users = accuntmodel.objects.all()
            for user in users :
                if user.melicode == meli :
                    name = user.firstname + ' ' + user.lastname
            for mesage in ms :
                if (mesage.vaziyat == "در انتظار پاسخ") and (mesage.sendermelicod == meli) and (int(mesage.recivermelicod) == int(request.user.username) ) :
                    messagenamber += 1
            for mes in ms :
                if (mes.sendermelicod == meli) and (mes.vaziyat == "در انتظار پاسخ") and (int(mesage.recivermelicod) == int(request.user.username)):
                    mestext = mes.textmessage
                    date = str(mes.hour) + ':' + str(mes.minute)
                    break
            meliarray.append(name)
            meliarray.append(date)
            meliarray.append(mestext)
            meliarray.append(messagenamber)
            nananswer.append(meliarray)

    # -------ارایه کامل پیامهای قدیم----
        ms = mesaagemodel.objects.all()
        for meli in ansphonnamberarray:
            name = ''
            # messagenamber = 0
            mestext = ''
            date = ''
            meliarray = ['']
            meliarray.clear()
            users = accuntmodel.objects.all()
            for user in users:
                if user.melicode == meli:
                    name = user.firstname + ' ' + user.lastname
            for mes in ms:
                if (mes.sendermelicod == meli) and (mes.vaziyat == "پاسخ داده شده"):
                    mestext = mes.textmessage
                    date = str(mes.hour) + ':' + str(mes.minute)
                    break
            meliarray.append(name)
            meliarray.append(date)
            meliarray.append(mestext)
            # meliarray.append(messagenamber)
            answer.append(meliarray)

        # nananswer.reverse()
        # answer.reverse()
        return render(request,'tiket.html',context={
                'nananswer':nananswer,
                'answer':answer,
                # 'listnonread':listmessage,
            })
    except:
        print("not netttttttttttttt")

    # t3 = Thread(target=tim, args="3")
    # t1.start()


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
            try:
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

            except:
                print("not net")
        # Schedule the message to be sent at midnight
        schedule.every().day.at("00:00").do(tavalod_tabrik)
        # schedule.every(5).seconds.do(tavalod_tabrik)
        while True:
            schedule.run_pending()
            time.sleep(1)
    if x == '2' :
        def yadavari_vaghtfarda():
            try:
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
            except:
                print("not net")
        # Schedule the message to be sent at midnight
        schedule.every().day.at("08:30").do(yadavari_vaghtfarda)
        # schedule.every(20).seconds.do(yadavari_vaghtfarda)
        while True:
            schedule.run_pending()
            time.sleep(1)
    if x == '3':
        def savemesaage():
            # if 1==1 :
            try:
                res = requests.post("https://api.kavenegar.com/v1/527064632B7931304866497A5376334B6B506734634E65422F627346514F59596C767475564D32656E61553D/sms/receive.json?linenumber=9982003178&isread=0")
                r = res.json()
                a = ['']
                a.clear()
                if 1 == 1:
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
                        if (aaa[0] != "2") and (aaa[0] != "1") :
                            users = accuntmodel.objects.all()
                            for user in users:
                                if int(user.phonnumber) == int(aaa[1]) :
                                    t = datetime.datetime.now()
                                    mesaagemodel.objects.create(
                                        recivermelicod='2259640788',
                                        vaziyat="در انتظار پاسخ",
                                        dateweek=strd(t),
                                        dateyear=stry(t),
                                        datemuonth=strb(t),
                                        dateday=stra(t),
                                        hour=t.strftime('%H'),
                                        minute=t.strftime('%M'),
                                        messagemethod=t.strftime('%S'),
                                        sendermelicod=str(user.melicode),
                                        textmessage= str(aaa[0]),
                                    )
            except:
                print("not net")
        schedule.every(60).seconds.do(savemesaage)
        while True:
            schedule.run_pending()
            time.sleep(1)


t1 = Thread(target=tim,args="1")
t2 = Thread(target=tim,args="2")
t3 = Thread(target=tim,args="3")
t1.start()
t2.start()
t3.start()
