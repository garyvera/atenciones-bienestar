from django.db import models


class MyManagerTotalNuevo (models.Manager):
   def get_queryset(self):
      return super(MyManagerTotalNuevo,self).get_queryset().filter(Estado = False)


     
