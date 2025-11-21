from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from Dashboard.models import Backlogs
from .forms import SupporteForms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def index(request):
    return render(request, "app/index.html")


@login_required
def about(request):
    return render(request, "app/about.html")


@login_required
def support(request):

    if request.method == "POST":
        form = SupporteForms(request.POST)
        if form.is_valid():
            suporte = form.save(commit=False)
            suporte.usuario = request.user
            suporte.save()

            messages.success(request, "Mensagem enviada com sucesso!")

            return redirect("support")
        else:
            messages.error(
                request, "Erro ao enviar. Verifique os campos e tente novamente!"
            )
    else:
        form = SupporteForms()

    return render(request, "app/support/support_problem.html", context={"form": form})


@login_required
def BacklogsListView(request):
    backlogs = Backlogs.objects.all().order_by("-data_postagem")

    itens_por_pagina = 2
    paginator = Paginator(backlogs, itens_por_pagina)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {"page_obj": page_obj}

    return render(request, "app/backlogs.html", context)
