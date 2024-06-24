from django.db import models

# Create your models here.
class Notificaciones(models.Model):
    titulo = models.CharField(max_length=50)
    fecha_recepcion = models.DateTimeField(auto_now_add=True)
    hora_recepcion = models.DateTimeField(auto_now=True)
    entidad = models.CharField(max_length=100)
    numero_exp = models.CharField(max_length=100) 
    dirigido_a = models.CharField(max_length=100) 
    recepcionista = models.CharField(max_length=100) 
    fecha_hora_entrega_interna = models.DateTimeField(null=True, blank=True)
    fecha_hora_entrega = models.DateTimeField(null=True, blank=True)


class Colaborador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

