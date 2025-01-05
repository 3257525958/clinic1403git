from django.db import models

class gharardadmodel(models.Model):
    melicod = models.CharField(max_length=10)
    type_select = models.CharField(max_length=20)
    job_select = models.CharField(max_length=50,default="0")
    cast = models.CharField(max_length=20)
    modirmelicod = models.CharField(max_length=10)
    day = models.CharField(max_length=5)
    muonth = models.CharField(max_length=20)
    year = models.CharField(max_length=5)
    def __str__(self):
        return f"{self.melicod}"

class pardakhtshodemodel(models.Model):
    peyment = models.CharField(max_length=20,default="0")
    off = models.CharField(max_length=20,default="0")
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

class savemovaghat(models.Model):
    hoghoghmelicod = models.CharField(max_length=11,default="0")
    idcod = models.CharField(max_length=10,default="0")

    def __str__(self):
        return f"{self.idcod}"

class esmekalamodel(models.Model):
    jobid = models.CharField(max_length=50,default="0")
    image = models.ImageField(upload_to='image/kala',null=True)
    esmekala = models.CharField(max_length=1000,default="0")
    berand = models.CharField(max_length=1000,default="0")
    unit = models.CharField(max_length=1000,default="0")
    value = models.CharField(max_length=1000,default='ندارد')

    def __str__(self):
        return f"{self.esmekala}"

class froshandemodel(models.Model):
    firstname = models.CharField(max_length=100 )
    lastname = models.CharField(max_length=100 )
    phonnumber = models.CharField(max_length=11 )
    def __str__(self):
        return f"{self.firstname}{' '}{self.lastname}"

class waremodel(models.Model):
    kala = models.CharField(max_length=200)
    froshande = models.CharField(max_length=150)
    castmethode = models.CharField(max_length=50,default='پرداخت نشده')
    cast =models.CharField(max_length=50 , default=0)
    value = models.CharField(max_length=50)
    year = models.CharField(max_length=5, default="0" , null=True)
    mounth = models.CharField(max_length=3, default="0" , null=True)
    day = models.CharField(max_length=3, default="0" , null=True)
    # -----------------اگر شماره فاکتور نداشته باشه 0 و اکه داشته باشه شماره فاکتور مذکور ثبت میشه-------------------
    factornumber = models.CharField(max_length=15, default="0" , null=True)
    # -------اگر تحوبل انبارشده باشه 1 و اگر نشده باشه 0 ثبت میشه-------------
    tahvil = models.CharField(max_length=2, default="0" , null=True)
    savermelicode = models.CharField(max_length=12, default="0" , null=True)
    takhfif =models.CharField(max_length=50, default="0")
    # -------------0 یعنی پرداخت نشده و 1 یعنی پرداخت شده-----------
    pardakht = models.CharField(max_length=50, default="0" , null=True)

    def __str__(self):
        return f"{self.kala}"
class anbarmodel(models.Model):
    kalaid = models.CharField(max_length=10)
    value = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.kalaid}"
class anbargardanimodel(models.Model):
    kalaid = models.CharField(max_length=10,default="0" , null=True)
    value = models.CharField(max_length=20,default="0" , null=True)
    dateyear= models.CharField(max_length=10,default="0" , null=True)
    datemounth= models.CharField(max_length=10,default="0" , null=True)
    dateday= models.CharField(max_length=10,default="0" , null=True)
    newvalue = models.CharField(max_length=10,default="0" , null=True)
    chengermelicode = models.CharField(max_length=11,default="0" , null=True)
    def __str__(self):
        return f"{self.kalaid}"


