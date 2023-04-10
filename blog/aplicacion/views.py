from django.shortcuts import render
from aplicacion.models import Persona, Posteo, Comentario
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
    return render(request, 'aplicacion/index.html')

def bloglist (request):
    return render(request, 'aplicacion/blog-list.html')

def blogpost (request):
    return render(request, 'aplicacion/blog-post.html')

def about (request):
    return render(request, 'aplicacion/about.html')

def listaPosteo(request):
    posteos = Posteo.objects.all()
    return render (request, "aplicacion/blog-list.html", {'posteos':posteos})

class PosteoCreacion(LoginRequiredMixin ,CreateView):
    model = Posteo
    success_url = "aplicacion/posteo_form.html"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']

class PosteoList(ListView):
    model = Posteo
    template_name = "aplicacion/blog-list.html"

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

            usuario.save()

            return render(request, "aplicacion/about.html", {"mensaje":"Se han modificado los datos de perfil"})

    else:

        perfilFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "aplicacion/editarPerfil.html", {"perfilFormulario": perfilFormulario, "usuario": usuario})
