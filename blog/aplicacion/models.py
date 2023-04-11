from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Persona (models.Model):
    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=250, null=True, blank=True)

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
    posteo = models.ForeignKey(Posteo, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    
class Avatar (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"

class Perfil (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    
class Detalle (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ForeignKey(Avatar, on_delete=models.RESTRICT, null=True, blank=True)
    descripcion = models.OneToOneField(Persona, on_delete=models.RESTRICT, null=True, blank=True, default="Ingrese aquí sus proyectos")
    mi_blog = models.CharField(max_length=400, null=True, blank=True, default="Ingrese aquí sus proyectos")
    habilidades = models.CharField(max_length=400, null=True, blank=True, default="Ingrese aquí sus proyectos")
    otros_proyectos = models.CharField(max_length=400, null=True, blank=True, default="Ingrese aquí sus proyectos")
    