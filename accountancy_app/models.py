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
    esmekala = models.CharField(max_length=1000,default="0")
    berand = models.CharField(max_length=1000,default="0")

    def __str__(self):
        return f"{self.esmekala}"

