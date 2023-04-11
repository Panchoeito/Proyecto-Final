from django import forms
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from aplicacion.models import Avatar, Persona


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
    
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Modificar email')
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repita la contraseña', widget= forms.PasswordInput)
    last_name = forms.CharField(label= 'Apellido', max_length=20, required=False)
    first_name = forms.CharField(label= 'Nombre', max_length=20, required=False)
    imagen = forms.ImageField(label= 'Imagen',required=False)
    descripcion = forms.CharField(label= 'Descripcion', required=False)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}
    
class DetalleEditForm (UserCreationForm):

    descripcion = forms.CharField(label='descripcion', max_length=400)
    mi_blog = forms.CharField(label='Acerca de mi blog',max_length=400)
    habilidades = forms.CharField(label='Hanilidades',max_length=400)
    otros_proyectos = forms.CharField(label='Otros proyectos',max_length=400)
        