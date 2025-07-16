from django.shortcuts import render
from .forms import UsuarioForm

def index(request):
    return render(request, "app/index.html")

def login(request):
    return render(request, "app/login.html")

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = UsuarioForm()
    else:
        form = UsuarioForm()
    
    return render(request, "app/login.html", {'form': form})

# Create your views here.
