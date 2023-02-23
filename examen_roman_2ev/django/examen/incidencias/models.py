from django.db import models

# Create your models here.
class Linea(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    color = models.CharField(max_length=200)
    distancia = models.IntegerField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre

class Estacion(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    lineas = models.ForeignKey(Linea, on_delete=models.CASCADE, related_name='lineas')

    def __str__(self):
        return self.nombre

class Incidencia(models.Model):
    texto = models.CharField(max_length=200)
    fecha = models.DateTimeField(null=False)
    estaciones = models.ForeignKey(Estacion, on_delete=models.CASCADE, related_name='estaciones')

    def __str__(self):
        return f"{self.estaciones} {self.texto}"