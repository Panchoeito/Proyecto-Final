from django import forms
from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from aplicacion.models import Avatar

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label= 'Nombre de Usuario')
    email = forms.EmailField(label= 'Correo electrónico')
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repite la contraseña', widget= forms.PasswordInput)
    last_name = forms.CharField(label= 'Apellido', max_length=20, required=False)
    first_name = forms.CharField(label= 'Nombre', max_length=20, required=False)
    imagen = forms.ImageField(label= 'Imagen', required=False)


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        labels = {'username':'nombre_usuario', 'email':'correo', 'last_name':'apellido', 'first_name':'nombre'}
        help_texts = {k:"" for k in fields}
