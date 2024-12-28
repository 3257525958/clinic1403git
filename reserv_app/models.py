from django.db import models


class reservemodel(models.Model):
    melicod =models.CharField(max_length=150,default='0')
    vaziyatereserv = models.CharField(max_length=12, default="رزرو")
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
    checking = models.CharField(max_length=20,default='false')
    vahed = models.CharField(max_length=100,default='0', null=True)
    idwork = models.CharField(max_length=100,default='0', null=True)
    bankpeyment = models.CharField(max_length=200, default='-3',null=True)
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
    message = models.CharField(max_length=20,default='0')
    cardnumber = models.CharField(max_length=20,default='0')
    rahgiricod = models.CharField(max_length=20,default='0')
    phonnumber = models.CharField(max_length=12,default='0')
    fiestname =models.CharField(max_length=150,default='0')
    lastname =models.CharField(max_length=150,default='0')
    vahed = models.CharField(max_length=100,default='')
    idwork = models.CharField(max_length=100,default='0', null=True)
    bankpeyment = models.CharField(max_length=200, default='-3',null=True)
    def __str__(self):
        return f"{self.personreserv}"

class leavemodel(models.Model):
    personelmelicod = models.CharField(max_length=11,default='0')
    dateshamsi = models.CharField(max_length=50,default='0')
    datemiladi = models.CharField(max_length=50,default='0')
    muont = models.CharField(max_length=50,default='0')
    leave = models.TextField (max_length=10000000000,default='0')


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
class filepage1model(models.Model):
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

class searchmodeltest(models.Model):
    m = models.CharField(max_length=20, default="0")

    def __str__(self):
        return f"{self.m}"


class fpeseshktestmodel(models.Model):
    melicod =models.CharField(max_length=15,default='0')
    jobreserv = models.CharField(max_length=150,default='0')
    detalereserv = models.CharField(max_length=150,default='0')
    personreserv = models.CharField(max_length=150,default='0')
    timereserv = models.CharField(max_length=15,default='0')
    castreserv = models.CharField(max_length=15,default='0')
    numbertime = models.CharField(max_length=10,default='0')
    hourreserv = models.CharField(max_length=10,default='0')
    dateshamsireserv = models.CharField(max_length=50,default='0')
    datemiladireserv = models.CharField(max_length=50,default='0')
    yearshamsi = models.CharField(max_length=10,default='0')
    cardnumber = models.CharField(max_length=20 ,default='0')
    pyment = models.CharField(max_length=20,default='0')
    trakingcod = models.CharField(max_length=20,default='0')
    bank = models.CharField(max_length=20,default='0')
    checking = models.CharField(max_length=20,default='false')
    apghablimage = models.ImageField(upload_to='image/apghabl',null=True)
    llateralghablimage = models.ImageField(upload_to='image/llateralghabl',null=True)
    apbadimage = models.ImageField(upload_to='image/apbad',null=True)
    llateralbadimage = models.ImageField(upload_to='image/llateralbad',null=True)
    rlateralbadimage = models.ImageField(upload_to='image/rlateralbad',null=True)
    coment = models.TextField (max_length=1000000,default='0')
    vahedeobject = models.CharField(max_length=10, default='1')
    vahedeobjectname = models.CharField(max_length=100, default='0',null=True)
    offer = models.CharField(max_length=20, default='0')
    reservid = models.CharField(max_length=50, default='0')
    materiyal = models.CharField(max_length=500, default='0')
    valueunit = models.CharField(max_length=200, default='0')
    bankpeyment = models.CharField(max_length=200, default='-3',null=True)

    def __str__(self):
        return f"{self.melicod}"



