from django.shortcuts import render

def reservdef(request):

    return render(request,'show_reserv.html',context={})