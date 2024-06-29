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
    idf = models.CharField(max_length=20,default="0")
    melicodvarizande = models.CharField(max_length=100,default='0')
    dateshamsi = models.CharField(max_length=100,default='0')
    datemiladi = models.CharField(max_length=100,default='0')
    filenumber = models.CharField(max_length=100,default='0')
    cashmethod = models.CharField(max_length=100,default='0')
    melicodeoperatore = models.CharField(max_length=100,default='0')
    mablagh = models.CharField(max_length=100,default='0')
    def __str__(self):
        return f"{self.filenumber}"


class casttestmodel(models.Model):
    p = models.CharField(max_length=20,default="0")
    s = models.CharField(max_length=100,default="0")
    c = models.CharField(max_length=100,default="0")
    def __str__(self):
        return f"{self.p}"
