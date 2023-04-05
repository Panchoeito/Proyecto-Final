from django.shortcuts import render
from aplicacion.models import Persona, Posteo, Comentario
from aplicacion.forms  import PosteoForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
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

class PosteoCreacion(CreateView):
    model = Posteo
    success_url = "aplicacion/blog-list.html"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']

class PosteoList(ListView):
    model = Posteo
    template_name = "aplicacion/blog-list.html"
