from django import forms
from django.utils import timezone
from django.contrib.auth.models import User


class PosteoForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=100)
    cuerpo = forms.CharField(max_length=4000)
    autor = forms.CharField(max_length=50)
    fecha = forms.DateTimeField()
    imagen = forms.ImageField(required=False)
    

class Comentario (forms.Form):
    
    comentario = forms.CharField(max_length=500)
    autor = forms.CharField()