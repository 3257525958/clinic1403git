from django.db import models
class fpeseshktestmodel(models.Model):
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
    checking = models.CharField(max_length=20,default='false')
    image = models.ImageField(upload_to='image/apghabl',null=True)
    image = models.ImageField(upload_to='image/llateralghabl',null=True)
    image = models.ImageField(upload_to='image/rlateralghabl',null=True)
    image = models.ImageField(upload_to='image/apbad',null=True)
    image = models.ImageField(upload_to='image/llateralbad',null=True)
    image = models.ImageField(upload_to='image/rlateralbad',null=True)
    coment = models.TextField(default='')
    vahedeobject = models.CharField(max_length=10, default='0')
    vahedeobjectname = models.CharField(max_length=10, default='0')
    offer = models.CharField(max_length=20, default='0')
    reservid = models.CharField(max_length=10, default='0')

    def __str__(self):
        return f"{self.personreserv}"