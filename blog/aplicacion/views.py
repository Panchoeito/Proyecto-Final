from django.shortcuts import render
from aplicacion.models import Persona, Posteo, Comentario, Perfil, Detalle, Avatar
from aplicacion.forms import UserEditForm, DetalleEditForm
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
        if avatares and descripcion:
            return render(request, 'aplicacion/index.html', {"url_imagen": avatares[0].imagen.url,"descripcion":descripcion[0]})
        elif descripcion:
            return render(request, 'aplicacion/index.html', {"descripcion":descripcion[0]})
        elif avatares:
            return render(request, 'aplicacion/index.html', {"url_imagen": avatares[0].imagen.url})
    else:
        return render(request, 'aplicacion/index.html')



def bloglist (request):
    return render(request, 'aplicacion/blog-list.html')




def about (request):
    return render(request, 'aplicacion/about.html')



class PosteoCreacion(LoginRequiredMixin ,CreateView):
    model = Posteo
    success_url = "/"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'fecha', 'imagen']
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    

class PosteoList(ListView):
    model = Posteo
    template_name = "aplicacion/blog-list.html"
    
    def form_valid(self, form):
        form.instance.imagen = self.request.user
        return super().form_valid(form), {"url_imagen": Posteo.imagen.url}
    


class blogpost (DetailView):
    
    model = Posteo
    template_name = "aplicacion/blog-post.html"
    
class EditarPerfil(LoginRequiredMixin, UpdateView):
    model = Perfil
    success_url = "/"
    fields = ['email', 'password1', 'last_name', 'first_name', 'last_name']

class VerPerfil (LoginRequiredMixin, DetailView):
    
    model = Detalle
    template_name = "aplicacion/about.html"
    
class EditarDetalle(LoginRequiredMixin, UpdateView):
    model = Detalle
    success_url = "aplicacion/about.html"
    fields = ['detalle', 'mi_blog', 'habilidades', 'otros_proyectos']

class ComentarioList(ListView):
    model = Comentario
    template_name = "aplicacion/blog-post.html"
class EditarComentario(LoginRequiredMixin, CreateView):

    model = Comentario
    success_url = reverse_lazy
    fields = ['comentario', 'autor', 'posteo', 'fecha']

@login_required
def editarDetalle(request):

    usuario = request.user

    if request.method == 'POST':

        detalleFormulario = DetalleEditForm(request.POST)

        if detalleFormulario.is_valid():

            informacion = detalleFormulario.cleaned_data

            usuario.Detalle.descripcion= informacion['descripcion']
            usuario.Detalle.mi_blog = informacion['mi_blog']
            usuario.Detalle.habilidades = informacion['habilidades']
            usuario.Detalle.otros_proyectos = informacion['otros_proyectos']



            usuario.save()

            return render(request, "aplicacion/about.html", {"mensaje":"Se han modificado los detalles"})

    else:

        detalleFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "aplicacion/editar-detalles.html", {"detalleFormulario": detalleFormulario, "usuario": usuario})

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

    return render(request, "aplicacion/editar-perfil.html", {"perfilFormulario": perfilFormulario, "usuario": usuario})

class CrearComentario(CreateView):
    model=Comentario
    success_url="blog-post"
    fields=['comentario', 'autor']