from django.db import models

# Create your models here.

class Persona (models.Model):
    
    email = models.EmailField()
    contrasenia = models.CharField(max_length=20)
    nombre_usuario = models.CharField(max_length=25, unique=True)
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return f"Usuario {self.nombre_usuario}, Contraseña: {self.contrasenia}"
    
class Posteo (models.Model):
    
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=4000)
    autor = models.ForeignKey('Persona', on_delete=models.RESTRICT, to_field="nombre_usuario")
    fecha = models.DateTimeField()
    imagen = models.ImageField()

class Comentario (models.Model):
    
    comentario = models.CharField(max_length=500)
    autor = models.ForeignKey('Persona', on_delete=models.RESTRICT, to_field="nombre_usuario")
    
