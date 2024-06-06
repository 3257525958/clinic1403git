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
