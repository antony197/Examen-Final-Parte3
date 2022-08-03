from django.db import models

# Create your models here.
class Producto(models.Model):
	codigo = models.TextField()
	nombre = models.TextField()
	precio_compra = models.TextField()
	precio_venta = models.TextField()
	Fecha_compra = models.TextField()
	Fecha_registro = models.DateTimeField(auto_now_add=True)
	estado =  models.TextField(max_length=1)

class Curso(models.Model):
     codigo = models.TextField()
     nombre = models.TextField()
     horas = models.TextField()
     creditos = models.TextField()
     fecha_registro = models.DateTimeField(auto_now_add=True)
     estado = models.CharField(max_length=1)