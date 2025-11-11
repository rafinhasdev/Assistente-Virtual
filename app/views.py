from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from Dashboard.models import Backlogs, SupportMensagens


@login_required
def index(request):
    return render(request, "app/index.html")


@login_required
def about(request):
    return render(request, "app/about.html")


@login_required
def listar_backlogs(request):
    backlogs = Backlogs.objects.all()
    context = {"backlogs": backlogs}
    return render(request, "app/backlogs.html", context)
