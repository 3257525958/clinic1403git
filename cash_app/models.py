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
    idf = models.CharField(max_length=20,default="0",null=True)
    melicodvarizande = models.CharField(max_length=10,default='0',null=True)
    dateshamsi = models.CharField(max_length=100,default='0',null=True)
    datemiladi = models.CharField(max_length=100,default='0',null=True)
    filenumber = models.CharField(max_length=100,default='0',null=True)
    cashmethodname = models.CharField(max_length=100,default='0',null=True)
    cashmethodid = models.CharField(max_length=100,default='0',null=True)
    melicodeoperatore = models.CharField(max_length=100,default='0',null=True)
    mablagh = models.CharField(max_length=500,default='0',blank=True,null=True)
    dateshamsieditor = models.CharField(max_length=500,default='0',null=True)
    bankpeyment = models.CharField(max_length=200, default='-3',null=True)


    def __str__(self):
        return f"{self.filenumber}"


class casttestmodel(models.Model):
    p = models.CharField(max_length=20,default="0")
    s = models.CharField(max_length=100,default="0")
    c = models.CharField(max_length=100,default="0")
    def __str__(self):
        return f"{self.p}"
class listmodeltest(models.Model):
    m = models.CharField(max_length=20,default="0")
    def __str__(self):
        return f"{self.m}"
class ctmodel(models.Model):
    idf = models.CharField(max_length=20,default="0")
    melicod = models.CharField(max_length=10,default="0")
    def __str__(self):
        return f"{self.idf}"

class hesabdaryaft(models.Model):
    firstname = models.CharField(max_length=50,null=True)
    lastname = models.CharField(max_length=50,null=True)
    onvansherkat = models.CharField(max_length=50,null=True)
    shomarehesabd = models.CharField(max_length=50,null=True)
    shomarekart = models.CharField(max_length=50,null=True)
    shomaresheba = models.CharField(max_length=50,null=True)
    idfroshander = models.CharField(max_length=5,null=True)

    def __str__(self):
        return f"{self.firstname}{' '}{self.lastname}"

