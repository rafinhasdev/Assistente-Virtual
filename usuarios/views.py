from .models import Usuarios
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm

# Create your views here.
def usuarios(request):
    usuarios = Usuarios.objects.all()
    context = {
        'usuarios': usuarios
    }
    return render(request, "app/dashboard/usuarios/usuarios.html", context)

def usuario_detail(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    context = {
        'usuario': usuario
    }
    return render(request, "app/dashboard/usuarios/usuarios_detail.html", context)

def usuarios_criar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = UsuarioForm()
            return redirect('usuarios')
    else:
        form = UsuarioForm()
    
    return render(request, "app/dashboard/usuarios/usuarios_criar.html", {'form': form})

def usuarios_editar(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    
    return render(request, "app/dashboard/usuarios/usuarios_editar.html", {'form': form})

def usuarios_remover(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    usuario.delete()
    return redirect('usuarios')