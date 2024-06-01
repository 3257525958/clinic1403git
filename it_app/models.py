from django.db import models


class mesaagetextmodel(models.Model):
    name = models.CharField(max_length=100,default="0")
    mesaagetext = models.TextField (max_length=900000,default="0")
    def __str__(self):
        return f"{self.name}"


class mesaagecuntermodel(models.Model):
    name = models.CharField(max_length=100,default="0")
    dateyear = models.CharField(max_length=100,default="0")
    datemuonth = models.CharField(max_length=100,default="0")
    dateday = models.CharField(max_length=100,default="0")
    dateweek = models.CharField(max_length=100,default="0")
    sender = models.CharField(max_length=100,default="0")
    cunt = models.CharField(max_length=100,default="0")
    def __str__(self):
        return f"{self.name}"


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

