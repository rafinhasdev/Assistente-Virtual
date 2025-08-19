from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm, SupporteForms, BacklogsForm
from .models import Backlogs, SupportMensagens, Usuarios


def index(request):
    return render(request, "app/index.html")


def backlogs(request):
    return render(request, "app/backlogs.html")

def about(request):
    return render(request, "app/about.html")

def login(request):
    return render(request, "app/login.html")

def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() ## AQUI ELE ENVIA OS DADOS PARA O FORMS. A IDEIA É TROCAR ESSE POR UMA FUNÇÃO DE CRIPTOGRAFIA E GERAR O TOKEN JWT
            form = UsuarioForm()
    else:
        form = UsuarioForm()
    
    return render(request, "app/login.html", {'form': form})

def att_backlogs(request):
    backlogs = Backlogs.objects.all()
    context = {
        'backlogs': backlogs
    }
    return render(request, "app/backlogs.html", context)

# Create your views here.

def dashboard(request):
    total_usuarios = Usuarios.objects.count()
    support = SupportMensagens.objects.all()
    total_backlogs = Backlogs.objects.count()

    context = {
        'total_usuarios': total_usuarios,
        'total_backlogs': total_backlogs,
        'support': support,
    }

    return render(request, "app/dashboard/dashboard.html", context)



# ------------------------------------- CRUD SUPORTE --------------------------------------------

def support(request):
    return render(request, "app/dashboard/suporte/support.html")


def support_listar(request):
    support = SupportMensagens.objects.all()
    context = {
        'support': support
    }
    return render(request, "app/dashboard/suporte/support.html", context)

def support_criar(request):
    if request.method == 'POST':
        form = SupporteForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = SupporteForms()
    else:
        form = SupporteForms()
    
    return render(request, "app/support/support.html", {'form': form})

def support_editar(request, pk):
    support = get_object_or_404(SupportMensagens, pk=pk)
    if request.method == 'POST':
        form = SupporteForms(request.POST, instance=support)
        if form.is_valid():
            form.save()
            return redirect('support_listar')
    else:
        form = SupporteForms(instance=support)
    
    return render(request, "app/support/support_editar.html", {'form': form})

def support_remover(request, pk):
    support = get_object_or_404(SupportMensagens, pk=pk)
    support.delete()
    return redirect('support_listar')

# ------------------------------------- CRUD SUPORTE --------------------------------------------
    
# ------------------------------------- CRUD USUARIOS --------------------------------------------

def usuarios(request):
    usuarios = Usuarios.objects.all()
    context = {
        'usuarios': usuarios
    }
    return render(request, "app/dashboard/usuarios/usuarios.html", context)

def usuario_detail(request, pk):
    usuario = get_list_or_404(Usuarios, pk=pk)
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

# ------------------------------------- CRUD USUARIOS --------------------------------------------

# ------------------------------------- CRUD BACKLOGS --------------------------------------------

def backlogs(request):
    backlogs = Backlogs.objects.all()
    context = {
        'backlogs': backlogs
    }
    return render(request, "app/dashboard/backlogs/backlogs.html", context)

def backlogs_criar(request):
    if request.method == 'POST':
        form = BacklogsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = BacklogsForm()
            return redirect('backlogs')
    else:
        form = BacklogsForm()
    
    return render(request, "app/dashboard/backlogs/backlogs_criar.html", {'form': form})

def backlogs_editar(request, pk):
    backlogs = get_object_or_404(Backlogs, pk=pk)
    if request.method == 'POST':
        form = BacklogsForm(request.POST, instance=backlogs)
        if form.is_valid():
            form.save()
            return redirect('backlogs')
    else:
        form = BacklogsForm(instance=backlogs)
    
    return render(request, "app/dashboard/backlogs/backlogs_criar.html", {'form': form})

def backlogs_remover(request, pk):
    backlogs = get_object_or_404(Backlogs, pk=pk)
    backlogs.delete()
    return redirect('backlogs')


# ------------------------------------- CRUD BACKLOGS --------------------------------------------