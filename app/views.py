from django.shortcuts import render, redirect, get_list_or_404
from .forms import UsuarioForm, SupporteForms
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
    return render(request, "app/support/support.html")

def support_listar(request):
    support = SupportMensagens.objects.all()
    context = {
        'support': support
    }
    return render(request, "app/support/support_listar.html", context)

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
    support = get_list_or_404(SupportMensagens, pk=pk)
    if request.method == 'POST':
        form = SupporteForms(request.POST, instance=support)
        if form.is_valid():
            form.save()
            return redirect('support_listar')
    else:
        form = SupporteForms(instance=support)
    
    return render(request, "app/support/support_editar.html", {'form': form})

def support_remover(request, pk):
    support = get_list_or_404(SupportMensagens, pk=pk)
    support.delete()
    return redirect('support_listar')

# ------------------------------------- CRUD SUPORTE --------------------------------------------
    
