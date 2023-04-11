from django.shortcuts import render
from aplicacion.models import Persona, Posteo, Comentario, Avatar
from login.forms import UserEditForm
from aplicacion.forms  import PosteoForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def index (request):

    if request.user.id:
        descripcion = Persona.objects.filter(user=request.user.id)
        avatares = Avatar.objects.filter(user=request.user.id)
        return render(request, 'aplicacion/index.html', {"url_imagen": avatares[0].imagen.url,"descripcion":descripcion[0]})
    else:
        return render(request, 'aplicacion/index.html')


def bloglist (request):
    return render(request, 'aplicacion/blog-list.html')




def about (request):
    return render(request, 'aplicacion/about.html')



class PosteoCreacion(LoginRequiredMixin ,CreateView):
    model = Posteo
    success_url = "/"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']

class PosteoList(ListView):
    model = Posteo
    template_name = "aplicacion/blog-list.html"

class blogpost (DetailView):
    
    model = Posteo
    template_name = "aplicacion/blog-post.html"
class EditarPerfil(LoginRequiredMixin, UpdateView):
    model = Persona
    success_url = "/"
    fields = ['email', 'password1', 'last_name', 'first_name', 'last_name', 'imagen','descripcion']
    
class EditarComentario(LoginRequiredMixin, CreateView):
    model = Comentario
    success_url = reverse_lazy
    fields = ['comentario', 'autor']

@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        perfilFormulario = UserEditForm(request.POST)

        if perfilFormulario.is_valid():

            informacion = perfilFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.imagen = informacion['imagen']

            usuario.save()

            return render(request, "aplicacion/about.html", {"mensaje":"Se han modificado los datos de perfil"})

    else:

        perfilFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "aplicacion/editar-perfil.html", {"perfilFormulario": perfilFormulario, "usuario": usuario})

class CrearComentario(CreateView):
    model=Comentario
    success_url="blog-post"
    fields=['comentario', 'autor']