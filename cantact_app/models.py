from django.db import models


class accuntmodel(models.Model):
    firstname = models.CharField(max_length=100 )
    berthday = models.CharField(max_length=20, default='0', null=True)
    lastname = models.CharField(max_length=100 )
    melicode = models.CharField(max_length=15 , default='0')
    phonnumber = models.CharField(max_length=11 )
    savesabt = models.CharField(max_length=100)
    pasword = models.CharField(max_length=100)
    level = models.CharField(max_length=50,default='دسترسی معمولی')
    dayb = models.CharField(max_length=3 , default='0')
    mountb = models.CharField(max_length=20 , default='0')
    yearb = models.CharField(max_length=5, default='0')
    def __str__(self):
        return f"{self.melicode}"
class savecodphon(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    melicode = models.CharField(max_length=20 , default="0")
    phonnumber = models.CharField(max_length=20 , default="0")
    berthdayyear = models.CharField(max_length=100)
    berthdayday = models.CharField(max_length=100)
    berthdaymounth = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    expaiercode = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.melicode}"



class dataacont(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    melicode = models.CharField(max_length=20 , default="0")
    phonnumber = models.CharField(max_length=20 , default="0")
    berthday = models.CharField(max_length=100)
    miladiarray = models.CharField(max_length=5000 , default="0")
    shamsiarray = models.CharField(max_length=5000 , default="0")
    showclandarray = models.CharField(max_length=5000 , default="0")
    def __str__(self):
        return f"{self.melicode}"


class phonnambermodel(models.Model):
    name = models.CharField(max_length=100,default="0")
    lastname = models.CharField(max_length=100, default="0")
    phonnumber = models.CharField(max_length=20 , default="0")
    saver = models.CharField(max_length=20 , default="0")
    def __str__(self):
        return f"{self.phonnumber}"
