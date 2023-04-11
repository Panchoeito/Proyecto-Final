from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Persona (models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.descripcion}"
    
class Posteo (models.Model):
    
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=4000)
    autor = models.ForeignKey(User, on_delete=models.RESTRICT)
    fecha = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='imagen_posteos', null=True, blank=True)

class Comentario (models.Model):
    
    comentario = models.CharField(max_length=500)
    autor = models.ForeignKey(User, on_delete=models.RESTRICT)
    
class Avatar (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"