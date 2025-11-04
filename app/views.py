from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, TemplateView, ListView
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required

from .forms import UsuarioForm, SupporteForms, BacklogsForm
from .models import Usuarios
from Dashboard.models import SupportMensagens, Backlogs



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

# ------------------------------------- LOGIN --------------------------------------------
                               
def callback(request):
    error = request.GET.get('error')

    if error:

        messages.error(request, "Autenticação negada.")
        return redirect('login')
    
    return redirect('index')

def login(request):
    return render(request, "app/login.html")

def logout(request):

    django_logout(request)
    return redirect('login')


