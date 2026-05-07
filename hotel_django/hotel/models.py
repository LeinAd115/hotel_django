from django.db import models

class Habitacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=50)
    imagen = models.URLField()

    def __str__(self):
        return self.nombre


class Reservacion(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    email = models.EmailField()
    habitacion = models.CharField(max_length=100)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()

    def __str__(self):
        return self.nombre_cliente