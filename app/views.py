from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, TemplateView, ListView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import UsuariosSerializer 
from .forms import UsuarioForm, SupporteForms, BacklogsForm, LoginForm
from .models import Backlogs, SupportMensagens, Usuarios


def index(request):
    return render(request, "app/index.html")

def about(request):
    return render(request, "app/about.html")


def listar_backlogs(request):
    backlogs = Backlogs.objects.all()
    context = {
        'backlogs': backlogs
    }
    return render(request, "app/backlogs.html", context)

def forms_support(request):
    if request.method == 'POST':
        form = SupporteForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = SupporteForms()
            return redirect('listar_backlogs')
    else:
        form = SupporteForms()
    
    return render(request, "app/support/support.html", {'form': form})

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


def login(request):
    return render(request, "app/login.html")


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

