from django.shortcuts import render
from cantact_app.models import *
from jobs_app.models import *
from accountancy_app.models import *
from cantact_app.views import *
import datetime
from cash_app.models import *
from accountancy_app.form import *


def aghdgharardad(request):
    melicod = request.POST.get('melicod')
    facebutton = request.POST.get('facebutton')
    us = accuntmodel.objects.all()
    savebottom = request.POST.get('savebottom')
    melicodetebar = "notr"
    etebar = ""
    if facebutton == 'accept':
        for u in us:
            if u.melicode == melicod :
                melicodetebar = "true"
                ws = workmodel.objects.all()
                works = ['']
                works.clear()
                for w in ws:
                    if w.person == u.firstname + ' ' + u.lastname :
                        works.append(w.work+' '+w.detalework)
                return render(request,'gharardad_aghd.html',context={
                                                                                'melicod':melicod,
                                                                                'melicodetebar':melicodetebar,
                                                                                'name':u.firstname +' '+u.lastname,
                                                                                'works':works,
                                                                                })
            melicodetebar = 'false'
    if savebottom == 'accept' :
        melicod = request.POST.get('melicod')
        type_select = request.POST.get('type_select')
        job_select = request.POST.get('job_select')
        cast = request.POST.get('cast')
        time = datetime.datetime.now()

        gharardadmodel.objects.create(melicod=melicod,
                                      type_select=type_select,
                                      job_select=job_select,
                                      cast=cast,
                                      modirmelicod=request.user.username,
                                      day=strd(time),
                                      muonth=strb(time),
                                      year=stry(time),
                                      )
        etebar = "true"

    return render(request,'gharardad_aghd.html',context={
                                                                    'melicodetebar':melicodetebar,
                                                                    'etebar':etebar,
                                                                    })# Create your views here.

def laghvgharardad(request):
    melicod = request.POST.get('melicod')
    facebutton = request.POST.get('facebutton')
    us = accuntmodel.objects.all()
    savebottom = request.POST.get('savebottom')
    melicodetebar = "notr"
    etebar = ""
    worklist = ['']
    worklist.clear()
    gs = gharardadmodel.objects.all()
    if facebutton == 'accept':
        for g in gs:
            if g.melicod == melicod:
                worklist.append(g.job_select +'   '+g.type_select+'   '+g.cast)

        for u in us:
            if u.melicode == melicod :
                melicodetebar = "true"
                return render(request,'gharardad_laghv.html',context={
                                                                                'melicod':melicod,
                                                                                'melicodetebar':melicodetebar,
                                                                                'name':u.firstname +' '+u.lastname,
                                                                                'worklist':worklist,
                                                                                })
            melicodetebar = 'false'
    if savebottom == 'accept' :
        melicod = request.POST.get('melicod')
        job_select = request.POST.get('job_select')
        gs = gharardadmodel.objects.all()
        for g in gs:
            if g.melicod == melicod:
                if (g.job_select + '   ' + g.type_select + '   ' + g.cast == job_select):
                    a = gharardadmodel.objects.filter(melicod=melicod,job_select=g.job_select)
                    a.delete()
        etebar = "true"

    return render(request,'gharardad_laghv.html',context={
                                                                    'melicodetebar':melicodetebar,
                                                                    'etebar':etebar,
                                                                    })# Create your views here.
def pardakhthoghogh(request):
    melicod = request.POST.get('melicod')
    if (melicod == None) or (melicod == '') :
        etebarmelicod = "notr"
    else:
        etebarmelicod = "false"
    us = accuntmodel.objects.all()
    name = ''
    for u in us:
        if melicod == u.melicode:
            name = u.firstname + ' ' + u.lastname
            etebarmelicod = "true"

    mounthselect = request.POST.get("mounthselect")
    etebar = ""

    notsel = request.POST.get("notsel")
    sel = request.POST.get("sel")
    tickon = request.POST.get("tickon")
    gs = gharardadmodel.objects.all()
    chekbox = "notselect"
    d = []
    d.clear()
    for g in gs:
        if g.melicod == melicod :
            if g.type_select == 'درصدی' :
                ps = castmodel.objects.all()
                for p in ps:
                    if (p.persone == melicod) and (p.selectjob == g.job_select) and (p.mounth == mounthselect):
                        dastmozddasadi = int(g.cast) * int(p.peyment)
                        dastmozddasadi = dastmozddasadi / 100
                        dd = ['']
                        dd.clear()
                        ss = savemovaghat.objects.all()
                        for s in ss:
                            if int(s.idcod) == int(p.id):
                                chekbox = "select"
                        dd = [p.selectjob,p.day+p.mounth+p.year,str(dastmozddasadi),chekbox,p.id]
                        chekbox = "notselect"
                        d.append(dd)
            if g.type_select == 'موردی' :
                ps = castmodel.objects.all()
                for p in ps :
                    if (p.persone == melicod) and (p.selectjob == g.job_select) and (p.mounth == mounthselect):
                        dastmozdmoredi = int(g.cast)
                        dm = ['']
                        dm.clear()
                        ss = savemovaghat.objects.all()
                        for s in ss:
                            if int(s.idcod) == int(p.id):
                                chekbox = "select"
                        dm = [p.selectjob,p.day+p.mounth+p.year,str(dastmozdmoredi),chekbox,p.id]
                        chekbox = "notselect"
                        d.append(dm)
    if (tickon != None) and (tickon != '') and (notsel != None) and (notsel != ''):
        j = int(tickon)
        c = 0
        for i in d:
            if c == j :
                i[3] = "select"
                savemovaghat.objects.create(hoghoghmelicod=melicod,idcod=i[4])
            c = c+1
    if  (sel != None) and (sel != ''):
        print("sel")
        print(sel)
        j = int(sel)
        c = 0
        for i in d:
            if c == j :
                i[3] = "notselect"
                a = savemovaghat.objects.filter(idcod=i[4],hoghoghmelicod=melicod)
                a.delete()
            c = c+1


    return render(request,'pardakht_hoghogh.html',context={
                                                                        'dastmozddasadimoredi':d,
                                                                        'mounthselect':mounthselect,
                                                                        'name':name,
                                                                        'etebarmelicod':etebarmelicod,
                                                                        'etebar':etebar,
                                                                        'melicod':melicod,
                                                                        # 'a':dd,
                                                                        })



def sana(request):
    job = request.POST.get('job')
    berand = request.POST.get("berand")
    esmekala =request.POST.get('esmekala')
    bottunesmekala =request.POST.get('bottunesmekala')
    value =request.POST.get('value')
    unit =request.POST.get('unit')
    js = jobsmodel.objects.all()
    jobsarray = ['']
    jobsarray.clear()
    form = esmekalaiform(request.POST, request.FILES)
    for j in js:
        p = (str(j.id) + "," + str(j.job)).split(",")
        jobsarray.append(p)
    if form.is_valid():
        form.save()
    # if (esmekala != None) and (esmekala != '') and (bottunesmekala == 'accept'):
    #     esmekalamodel.objects.create(esmekala=esmekala, berand=berand , jobid=job , unit=unit ,value=value)
    return render(request,'sana.html',context={
        'jobsarray':jobsarray,
        'form':form,
        })