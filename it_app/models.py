from django.db import models


class mesaagetextmodel(models.Model):
    name = models.CharField(max_length=100,default="0")
    mesaagetext = models.TextField (max_length=900000,default="0")
    def __str__(self):
        return f"{self.name}"


class mesaagemodel(models.Model):
    melicod = models.CharField(max_length=11,default="0")
    vaziyat = models.CharField(max_length=30,default="در انتظار پاسخ")
    dateweek = models.CharField(max_length=11,default="0")
    dateyear = models.CharField(max_length=100,default="0")
    datemuonth = models.CharField(max_length=100,default="0")
    dateday = models.CharField(max_length=100,default="0")
    hour = models.IntegerField(max_length=2,default=0)
    minute = models.IntegerField(max_length=2,default=0)
    messagemethod = models.CharField(max_length=11,default="پیامک")
    sendermelicod = models.CharField(max_length=10,default="0")
    textmessage = models.TextField(max_length=1000000,default="0")

    def __str__(self):
        return f"{self.melicod}"


class homeimgmodel(models.Model):
    name = models.CharField(max_length=100,default="0", null=True)
    image = models.ImageField(upload_to='image/homepc',null=True)
    def __str__(self):
        return f"{self.name}"
class homemenosarimodel(models.Model):
    name = models.CharField(max_length=100,default="0", null=True)
    image = models.ImageField(upload_to='image/menosari',null=True)

    def __str__(self):
        return f"{self.name}"

class homemobilemodel(models.Model):
    name = models.CharField(max_length=100,default="0", null=True)
    image = models.ImageField(upload_to='image/homemobile',null=True)
    def __str__(self):
        return f"{self.name}"

