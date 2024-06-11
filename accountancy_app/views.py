from django.shortcuts import render
from cantact_app.models import *
from jobs_app.models import *
from accountancy_app.models import *
from cantact_app.views import *
import datetime
from cash_app.models import *


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



    d = ['']
    d.clear()
    gs = gharardadmodel.objects.all()
    chekbox = "notselect"
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
                        dd = [p.selectjob,p.day+p.mounth+p.year,str(dastmozddasadi),chekbox,p.id]
                        d.append(dd)
            if g.type_select == 'موردی' :
                ps = castmodel.objects.all()
                for p in ps :
                    if (p.persone == melicod) and (p.selectjob == g.job_select) and (p.mounth == mounthselect):
                        dastmozdmoredi = int(g.cast)
                        dm = ['']
                        dm.clear()
                        dm = [p.selectjob,p.day+p.mounth+p.year,str(dastmozdmoredi),chekbox,p.id]
                        d.append(dm)
    check = request.POST.get("check")
    # savemovaghat.objects.create(hoghoghmelicod=d[int(check)][])
    if (check != None) and (check != ''):
        # d[int(check)][3] = "select"
        a = d[int(check)]
        b = a[0]
        print(b)
        b = a[1]
        print(b)
        b = a[2]
        print(b)
        b = a[3]
        print(b)
    return render(request,'pardakht_hoghogh.html',context={
                                                                        'dastmozddasadimoredi':d,
                                                                        'mounthselect':mounthselect,
                                                                        'name':name,
                                                                        'etebarmelicod':etebarmelicod,
                                                                        'etebar':etebar,
                                                                        'melicod':melicod,
                                                                        })



def sana(request):
    return render(request,'sana.html')