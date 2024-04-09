from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Carrera, Nivel

class CarreraResources(resources.ModelResource):
        class Meta: 
            model = Carrera
            import_id_fields = ('codigo',)
          
            fields = (
              'codigo', 
              'carrera',
              )
            
class CarreraAdmin(ImportExportModelAdmin):
    resource_classes = [CarreraResources]
    list_display = ('codigo', 'carrera')
    ordering = ['carrera']
    search_fields=['carrera']
admin.site.register(Carrera, CarreraAdmin)



   



