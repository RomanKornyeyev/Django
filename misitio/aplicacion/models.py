from django.db import models

# Create your models here.
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=250)
    foto = models.ImageField(upload_to="aplicacion/", blank=True, null=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    bibliotecas = models.ManyToManyField(Biblioteca)

    def __str__(self):
        valor = ", ".join(str(v) for v in self.bibliotecas.all())
        return f"{self.titulo} ({valor})"