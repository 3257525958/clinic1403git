from django.db import models

class bankmodel(models.Model):
    onvan = models.CharField(max_length=100)
    officnamber = models.CharField(max_length=100)
    namberkart = models.CharField(max_length=100)
    shebanamber = models.CharField(max_length=100)
    melicodebank = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.onvan}"
class castmodel(models.Model):
    peyment = models.CharField(max_length=100,default="0")
    melicodevarizande = models.CharField(max_length=11,default="0")
    selectjob = models.CharField(max_length=100,default="0")
    bankonvan = models.CharField(max_length=100,default="0")
    persone = models.CharField(max_length=100,default="0")
    operatore = models.CharField(max_length=11,default="0")
    day = models.CharField(max_length=100,default="0")
    mounth = models.CharField(max_length=100,default="0")
    year = models.CharField(max_length=100,default="0")
    def __str__(self):
        return f"{self.melicodevarizande}"
