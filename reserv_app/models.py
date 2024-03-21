from django.db import models


class reservemodel(models.Model):
    melicod =models.CharField(max_length=150,default='0')
    jobreserv = models.CharField(max_length=150,default='0')
    detalereserv = models.CharField(max_length=150,default='0')
    personreserv = models.CharField(max_length=150,default='0')
    timereserv = models.CharField(max_length=150,default='0')
    castreserv = models.CharField(max_length=150,default='0')
    numbertime = models.CharField(max_length=10,default='0')
    hourreserv = models.CharField(max_length=10,default='0')
    dateshamsireserv = models.CharField(max_length=150,default='0')
    datemiladireserv = models.CharField(max_length=150,default='0')
    yearshamsi = models.CharField(max_length=10,default='0')
    cardnumber = models.CharField(max_length=20 ,default='0')
    pyment = models.CharField(max_length=20,default='0')
    trakingcod = models.CharField(max_length=20,default='0')
    bank = models.CharField(max_length=20,default='0')
    def __str__(self):
        return f"{self.personreserv}"

class reservemodeltest(models.Model):
    mellicode = models.CharField(max_length=12, default="0")
    jobreserv = models.CharField(max_length=150,default='0')
    detalereserv = models.CharField(max_length=150,default='0')
    personreserv = models.CharField(max_length=150,default='0')
    timereserv = models.CharField(max_length=150,default='0')
    castreserv = models.CharField(max_length=150,default='0')
    numbertime = models.CharField(max_length=10,default='0')
    hourreserv = models.CharField(max_length=10,default='0')
    dateshamsireserv = models.CharField(max_length=150,default='0')
    datemiladireserv = models.CharField(max_length=150,default='0')
    yearshamsi = models.CharField(max_length=10,default='0')
    def __str__(self):
        return f"{self.personreserv}"

class leavemodel(models.Model):
    personelmelicod = models.CharField(max_length=11,default='0')
    dateshamsi = models.CharField(max_length=50,default='0')
    datemiladi = models.CharField(max_length=50,default='0')
    muont = models.CharField(max_length=50,default='0')
    leave = models.CharField (max_length=630,default='0')


class neursemodel(models.Model):
    mellicode = models.CharField(max_length=12, default="0")
    inject_botax = models.CharField(max_length=150,default='0')
    illnes = models.CharField(max_length=150,default='0')
    drug = models.CharField(max_length=150,default='0')
    sensivety = models.CharField(max_length=150,default='0')
    pregnancy = models.CharField(max_length=150,default='0')
    date_finaly = models.CharField(max_length=150,default='0')
    image_show = models.CharField(max_length=150,default='0')
    satisfact = models.CharField(max_length=150,default='0')
    def __str__(self):
        return f"{self.mellicode}"
class neursetestmodel(models.Model):
    mellicode = models.CharField(max_length=12, default="0")
    inject_botax = models.CharField(max_length=150,default='0')
    illnes = models.CharField(max_length=150,default='0')
    drug = models.CharField(max_length=150,default='0')
    sensivety = models.CharField(max_length=150,default='0')
    pregnancy = models.CharField(max_length=150,default='0')
    date_finaly = models.CharField(max_length=150,default='0')
    image_show = models.CharField(max_length=150,default='0')
    satisfact = models.CharField(max_length=150,default='0')
    def __str__(self):
        return f"{self.mellicode}"
