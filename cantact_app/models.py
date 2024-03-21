from django.db import models


class accuntmodel(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    melicode = models.CharField(max_length=10 , default='0')
    phonnumber = models.CharField(max_length=11 , default='0')
    berthday = models.CharField(max_length=100)
    pasword = models.CharField(max_length=100)
    level = models.CharField(max_length=50,default='دسترسی معمولی')
    def __str__(self):
        return f"{self.melicode}"
class savecodphon(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    melicode = models.CharField(max_length=20 , default="0")
    phonnumber = models.CharField(max_length=20 , default="0")
    berthday = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    expaiercode = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.melicode}"
