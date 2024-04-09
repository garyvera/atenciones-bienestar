from django.db import models

# Create your models here.
class Carrera (models.Model):
    codigo = models.CharField(max_length=50, primary_key=True)
    carrera = models.CharField(max_length=50)
    def __str__(self):
        return self.carrera

class Nivel (models.Model):
    nivel = models.IntegerField()
    codigo = models.ManyToManyField(Carrera)
    
    def __int__(self):
       return self.codigo
    