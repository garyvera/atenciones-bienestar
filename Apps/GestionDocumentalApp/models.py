from django.db import models

opciones = (('1', 'Recibido'),
            (2, 'Atendido'),
            (3, 'Archivado'),
            (4, 'S/N'))
# Create your models here.

class SeccionSucceion(models.Model):
    seccionsubseccion= models.CharField(max_length=250)
   
    def __str__(self):
        return self.seccionsubseccion
class Departamento(models.Model):
    departamento = models.CharField(max_length=100)
    seccionsubdepartamento = models.ManyToManyField(SeccionSucceion)
    def __str__(self):
        return self.departamento
    
class Tipodocumento(models.Model):
    tipodocumento = models.CharField(max_length=255)
    def __str__(self):
        return self.tipodocumento

class Documento(models.Model):
    electronico =  models.BooleanField(default=True)
    titulo = models.CharField(max_length=255, unique=True)
    fecha = models.DateField(blank=True, null=True)
    descripcion= models.TextField(max_length=255)
    tipodocumento= models.ForeignKey(Tipodocumento, default= 1, on_delete=models.CASCADE)
    hojas = models.IntegerField(default=1)
    estadotramite = models.CharField(max_length=1, choices=opciones, default=4)
    def __str__(self):
        return self.titulo

class Serie (models.Model):
    serie = models.CharField(max_length=255, unique=True, verbose_name="Serie")
    def __str__(self):
        return self.serie
    
class SubSerie (models.Model):
    subserie = models.CharField(max_length=255, unique=True, verbose_name="Sub Serie")
    serie = models.ForeignKey(Serie,on_delete=models.CASCADE)
    def __str__(self):
        return self.subserie
  
class Expediente (models.Model):
    expediente = models.CharField(max_length=255, unique=True)
    fechainicio = models.DateField()
    def __srt__(self):
        return self.expediente
    
class TipoExpediente (models.Model):
    tipoexpediente = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.tipoexpediente
class DetalleExpediente(models.Model):
    tipoexpedetalle = models.ForeignKey(TipoExpediente, on_delete=models.CASCADE) 
    expedientedetalle = models.ForeignKey(Expediente, on_delete=models.CASCADE)
    documentoexpediente = models.ForeignKey(Documento, on_delete=models.CASCADE)
    tipodocumentodetalle= models.ForeignKey(Tipodocumento, on_delete=models.CASCADE)
    departamentodetalle= models.ForeignKey(Departamento, on_delete=models.CASCADE)
    subseriedetalle= models.ForeignKey(SubSerie, on_delete=models.CASCADE)
    fechafin = models.DateField(blank=True, null=True)
    def __int__(self):
        return self.tipoexpedetalle