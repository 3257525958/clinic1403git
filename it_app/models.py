from django.db import models


class mesaagetextmodel(models.Model):
    name = models.CharField(max_length=100)
    mesaagetext = models.TextField (max_length=900000)
    def __str__(self):
        return f"{self.name}"


class mesaagecuntermodel(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    sender = models.CharField(max_length=100)
    cunt = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
