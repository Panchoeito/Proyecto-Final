from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'aplicacion/index.html')

def bloglist (request):
    return render(request, 'aplicacion/blog-list.html')

def blogpost (request):
    return render(request, 'aplicacion/blog-post.html')

def about (request):
    return render(request, 'aplicacion/about.html')
