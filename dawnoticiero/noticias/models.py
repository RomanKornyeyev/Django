from django.db import models

# Create your models here.
# class Noticia extends Model
class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    foto1 = models.ImageField(upload_to='noti', null=False)
    foto2 = models.ImageField(upload_to='noti', blank=True)
    foto3 = models.ImageField(upload_to='noti', blank=True)
    foto4 = models.ImageField(upload_to='noti', blank=True)
    foto5 = models.ImageField(upload_to='noti', blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.fecha})"
    
    def getImages(self):
        return [self.foto1, self.foto2, self.foto3, self.foto4, self.foto5]