from django.shortcuts import render

def sendmesaage(request):
    return render(request,'mesage_send.html')
def savemesaage(request):

    return render(request,'mesaage_save.html')