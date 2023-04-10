from django import forms

class PosteoForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=100)
    cuerpo = forms.CharField(max_length=4000)
    autor = forms.CharField(max_length=50)
    fecha = forms.DateTimeField()
    imagen = forms.ImageField()