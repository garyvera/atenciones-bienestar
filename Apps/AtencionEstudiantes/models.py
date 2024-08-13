from django.db import models

# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    SEXO = [
        ("1", "HOMBRE"),
        ("2", "MUJER"),
        ("3", "NO BINARIO"),
]
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    dni = models.CharField(max_length=10, unique=True)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    nombre = models.CharField(max_length=100)
    sexo = models.CharField(max_length=2, choices=SEXO)
    
    def __str__(self):
        return f" {self.carrera}  {self.dni} {self.nombre} {self.apellido_paterno} {self.apellido_materno}"

class Atencion(models.Model):
    DETALLE = [
        ("1", "APOYO SOCIOECONOMICO (BECAS)"),
        ("2", "ORIENTACIÓN VOCACIONAL Y DESARROLLO"),
        ("3", "ATENCIÓN PSICOLÓGICA"),
        ("4", "SEGURO ESTUDIANTIL"),
        ("5", "MEDIACIÓN"),
        ("6", "TRABAJO SOCIAL"),
        ("7", "INCLUSIÓN"),
        ("8", "ATENCIÓN MÉDICA"),
        ("9", "ATENCIÓN ODONTOLÓGICA"),
        ("10", "DEPORTE"),
        ("11", "MÚSICA"),
        ("12", "DANZA"),
    ]

    NIVEL = [
        ("1", "PRIMER"),
        ("2", "SEGUNDO"),
        ("3", "TERCER"),
        ("4", "CUARTO"),
        ("5", "QUINTO"),
        ("6", "SEXTO"),
        ("7", "SEPTIMO"),
        ("8", "OCTAVO"),
        ("9", "NOVENO"),
        ("10", "DECIMO"),
        
    ]

    OPCIONES = [
        ("1", "MUY BUENA"),
        ("2", "BUENA"),
        ("3", "REGULAR"),
    ]

    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    nivel = models.CharField(max_length=2, choices=NIVEL)
    motivo = models.CharField(max_length=2, choices=DETALLE)
    encuesta = models.CharField(max_length=2, choices=OPCIONES, null=True, blank=True, default="___")
    fecha = models.DateField(blank=True, null=False, auto_now=True, )
    
    def __str__(self):
        return self.motivo
    





    



