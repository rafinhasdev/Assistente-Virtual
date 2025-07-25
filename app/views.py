from django.shortcuts import render
from .forms import UsuarioForm, SupporteForms
from .models import Backlogs


def index(request):
    return render(request, "app/index.html")

def support(request):
    return render(request, "app/support.html")

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

def criar_support(request):
    if request.method == 'POST':
        form = SupporteForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = SupporteForms()
    else:
        form = SupporteForms()
    
    return render(request, "app/support.html", {'form': form})

def att_backlogs(request):
    backlogs = Backlogs.objects.all()
    context = {
        'backlogs': backlogs
    }
    return render(request, "app/backlogs.html", context)

# Create your views here.
