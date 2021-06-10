from django.db import models

# Create your models here.



class Calendario(models.Model):
    id_evento = models.AutoField(primary_key = True)
    fecha_ev = models.DateTimeField()
    #agregar antecedentes
    contenido = models.CharField(max_length = 150, blank = True)

    def __str__ (self):
        return (self.contenido)

class Antecedentes(models.Model):
    id_ed = models.AutoField(primary_key = True)
    fecha_mod = models.DateTimeField()
    id_evento = models.ForeignKey(Calendario,on_delete = models.CASCADE)
    #no_control = models.CharField(max_length = 13)



