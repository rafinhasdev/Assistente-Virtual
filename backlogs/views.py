from django.shortcuts import render, redirect, get_object_or_404
from .forms import BacklogsForm
from .models import Backlogs

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
# Create your views here.
