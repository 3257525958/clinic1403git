from django.shortcuts import render
from cantact_app.models import *
from jobs_app.models import *
from accountancy_app.models import *
from cantact_app.views import *
import datetime


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
                print("1")
                if (g.job_select + '   ' + g.type_select + '   ' + g.cast == job_select):
                    print("2")
                    a = gharardadmodel.objects.filter(melicod=melicod,job_select=g.job_select)
                    a.delete()
        etebar = "true"

    return render(request,'gharardad_laghv.html',context={
                                                                    'melicodetebar':melicodetebar,
                                                                    'etebar':etebar,
                                                                    })# Create your views here.
