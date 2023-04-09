from django.shortcuts import render
from aplicacion.models import Persona
from login.forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username = username, password = password)
            
            if user is not None:
                
                login(request,user)
                
                return render (request, "aplicacion/index.html", {"mensaje": f"Bienvenido/a {username}"})
            
            else:
                
                return render(request, "login/login.html", {"mensaje":"Error en los datos ingresados"})
        
        else:
                
            return render(request, "login/login.html", {"mensaje":"Formulario erroneo"})
        
    form = AuthenticationForm()
        
    return render(request, "login/login.html", {'form': form})
    
def register(request):
    
    if request.method == "POST":
        
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()
            return render(request, "aplicacion/index.html", {"mensaje":"Usuario Creado"})
    
    else:
        form = UserRegisterForm()
        
    return render(request, "login/registro.html", {"form":form})
