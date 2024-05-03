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
    peyment = models.CharField(max_length=100)
    melicodevarizande = models.CharField(max_length=100)
    selectjob = models.CharField(max_length=100)
    bankonvan = models.CharField(max_length=100)
    persone = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    mounth = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.melicodevarizande}"
