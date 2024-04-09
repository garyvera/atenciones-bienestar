from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from Apps.GestionDocumentalApp.models import DetalleExpediente,Documento
#from django.views.generic import ListView
#from   .models import DocumentoNuevo
# Create your views here.
#def plantilla (request):
   #documentos_listados = DocumentoNuevo.objects.filter(Documento = True)
   #contar1 = DocumentoNuevo.objects.filter(Documento = True).count()
   #return render (request, "prueba.html", {"documento": documentos_listados, "contar": contar1})

#def plantilla1 (request):
 #dato= DocumentoNuevo.objects.all().values()
 #datospanda = pd.DataFrame(dato)
 #grafico = pd.date_range("20130101", periods=6)

 #diccionario ={

  #  "datos":grafico.to_html()
 #}
 #return render (request, 'prueba.html', context=diccionario)
 
class indexPageView(ListView):
    template_name = "prueba.html"
    model = DetalleExpediente