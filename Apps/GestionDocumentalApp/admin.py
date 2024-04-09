from django.contrib import admin

from .models import Departamento, SeccionSucceion, Tipodocumento,Documento,Serie,SubSerie,Expediente,TipoExpediente,DetalleExpediente
 
# Register your models here.

@admin.register(Departamento)
class AdminDepartamento(admin.ModelAdmin):
   list_display = ('departamento',)

@admin.register(SeccionSucceion)
class AdminSecSub(admin.ModelAdmin):
   list_display = ('seccionsubseccion',)

@admin.register(Tipodocumento)
class AdminTipoDocumento(admin.ModelAdmin):
   list_display = ('tipodocumento',)

@admin.register(Documento)
class AdminDocumento(admin.ModelAdmin):
   list_display = ('titulo',)

@admin.register(Serie)
class AdminSerie(admin.ModelAdmin):
   list_display = ('serie',)
  
@admin.register(SubSerie)
class AdminSubSerie(admin.ModelAdmin):
   list_display = ('subserie',)

@admin.register(Expediente)
class AdminExpediente(admin.ModelAdmin):
   list_display = ('expediente',)

@admin.register(TipoExpediente)
class AdminTipoexpediente(admin.ModelAdmin):
   list_display = ('tipoexpediente',)

@admin.register(DetalleExpediente)
class AdminDetalleexpediente(admin.ModelAdmin):
   list_display = ('tipoexpedetalle','documentoexpediente', 'tipodocumentodetalle', 'departamentodetalle','subseriedetalle','fechafin','expedientedetalle',)
