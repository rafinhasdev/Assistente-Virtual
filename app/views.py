from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Dashboard.models import SupportMensagens, Backlogs

@login_required
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



