from django.shortcuts import render, redirect, get_object_or_404
from .models import SupportMensagens
from .forms import SupporteForms

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
