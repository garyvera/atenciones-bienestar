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
   list_display = ['nombre', 'dni']
   search_fields=['dni']
   #readonly_fields = ('nombre','dni')
admin.site.register(Estudiante, EstudianteAdmin)

class CarreraAdmin(ImportExportModelAdmin):
    
   list_display = ['nombre']
admin.site.register(Carrera, CarreraAdmin)

class RegistroResource(resources.ModelResource):
    carrera = fields.Field(
        column_name='CARRERA',
        attribute='carrera',
        widget=ForeignKeyWidget(Carrera, field='nombre')
        )
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

    column_name='ESTUDIANTE',
    class Meta:
        model = Atencion
        fields = ('dni', 'full_title', 'sexo_name', 'nivel_name', 'motivo', 'fecha',)
        export_order = ('dni', 'full_title', 'sexo_name', 'nivel_name', 'motivo', 'fecha', )

    def dehydrate_sexo_name(self, atencion):
        return atencion.estudiante.get_sexo_display()
    

    def dehydrate_full_title(self, atencion):
        name = getattr(atencion.estudiante, "nombre",)
        ap1 = getattr(atencion.estudiante, "apellido_paterno",)
        ap2 = getattr(atencion.estudiante, "apellido_materno",)
        return '%s  %s  %s' % (name, ap1, ap2 )

    def nivel(self, obj):
        return obj.atencion.get_nivel_display()
    nivel.short_description = 'nivel'
   

class AtencionAdmin(ImportExportModelAdmin):
   resource_class= (RegistroResource)
   list_display = ['dni', 'ESTUDIANTE', 'sexo','nivel','motivo','fecha',]
   search_fields = ['estudiante__dni']
   list_filter = ['fecha','motivo']
   raw_id_fields = ['estudiante']
   
   def dni(self, obj):
        return obj.estudiante.dni
   def sexo(self, obj):
        return obj.estudiante.get_sexo_display()
   sexo.short_description = 'Sexo'
   
   def ESTUDIANTE(self, atencion):
        name = getattr(atencion.estudiante, "nombre",)
        ap1 = getattr(atencion.estudiante, "apellido_paterno",)
        ap2 = getattr(atencion.estudiante, "apellido_materno",)
        return '%s  %s  %s' % (name, ap1, ap2 )
   
admin.site.register(Atencion, AtencionAdmin)
