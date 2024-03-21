from django.db import models



class storemodel(models.Model):
    nameofmaterial = models.CharField(max_length=150 , default='None')
    numberofmaterial = models.CharField(max_length=10,default='0')
    def __str__(self):
        return f"{self.nameofmaterial}"
