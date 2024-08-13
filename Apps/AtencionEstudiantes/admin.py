from django.contrib import admin
# Register your models here.
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from django.contrib import admin
from .models import Estudiante, Carrera, Atencion
from import_export.widgets import ForeignKeyWidget
from import_export.fields import Field
from django.utils import formats

class EstudianteAdmin(ImportExportModelAdmin):
   list_display =  ['dni','apellido_paterno', 'apellido_materno', 'nombre', 'carrera']
   search_fields=  ['dni','apellido_paterno','apellido_materno','nombre']
   #readonly_fields = ('nombre','dni')
admin.site.register(Estudiante, EstudianteAdmin)

class CarreraAdmin(ImportExportModelAdmin):
   list_display = ['nombre', ]
admin.site.register(Carrera, CarreraAdmin)

class RegistroResource(resources.ModelResource):
    dni = fields.Field(
        column_name='# CEDULA',
        attribute='estudiante',
        widget=ForeignKeyWidget(Estudiante, field='dni')
        )

    full_title = fields.Field(
        column_name='ESTUDIANTE',
    )
    nivel_name = fields.Field(
        column_name='NIVEL',
        attribute='get_nivel_display'
    )
    
    sexo_name = fields.Field(
        column_name='SEXO',
    )
    
    motivo = fields.Field(
        column_name='MOTIVO',
        attribute='get_motivo_display'
    )
    fecha = fields.Field(
        column_name='FECHA',
        attribute='fecha',
    )
    
    encuesta = fields.Field(
        column_name='ATENCIÓN',
        attribute='get_encuesta_display',
    )


    carrera_name = fields.Field(
        column_name='CARRERA',
        attribute='estudiante__carrera__nombre',  # Acceder al nombre de la carrera a través de la relación
    )
    class Meta:
        model = Atencion
        fields = ('dni', 'full_title',  'sexo_name', 'nivel_name', 'motivo', 'fecha', 'carrera_name', 'encuesta', )
        export_order = ('dni', 'full_title', 'sexo_name', 'carrera_name','nivel_name', 'motivo', 'fecha', 'encuesta', )

    def dehydrate_sexo_name(self, atencion):
        return atencion.estudiante.get_sexo_display()
    
    def dehydrate_carrera_name(self, atencion):
        return atencion.estudiante.get_carrera_display()
    
    def dehydrate_full_title(self, atencion):
        name = getattr(atencion.estudiante, "nombre",)
        ap1 = getattr(atencion.estudiante, "apellido_paterno",)
        ap2 = getattr(atencion.estudiante, "apellido_materno",)
        return '%s  %s  %s' % (name, ap1, ap2 )
    
    def dehydrate_carrera_name(self, atencion):
        return atencion.estudiante.carrera.nombre

    def nivel(self, obj):
        return obj.atencion.get_nivel_display()
    nivel.short_description = 'nivel'
   
class AtencionAdmin(ImportExportModelAdmin):
   resource_class= (RegistroResource)
   list_display = ['dni', 'ESTUDIANTE', 'carrera', 'sexo','nivel','motivo','fecha', 'encuesta']
   search_fields = ['estudiante__dni']
   list_filter = ['fecha','motivo', 'estudiante__carrera', ]
   raw_id_fields = ['estudiante']
 
   
   def dni(self, obj):
        return obj.estudiante.dni
   def carrera(self, obj):
        return obj.estudiante.carrera
   def sexo(self, obj):
        return obj.estudiante.get_sexo_display()
   sexo.short_description = 'Sexo'

   def ESTUDIANTE(self, atencion):
        name = getattr(atencion.estudiante, "nombre",)
        ap1 = getattr(atencion.estudiante, "apellido_paterno",)
        ap2 = getattr(atencion.estudiante, "apellido_materno",)
        return '%s  %s  %s' % (name, ap1, ap2 )
   
admin.site.register(Atencion, AtencionAdmin)

