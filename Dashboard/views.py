from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Backlogs, SupportMensagens, Usuarios
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'dashboard/index.html')


@login_required
class BacklogsListView(ListView):
    model = Backlogs
    template_name = 'dashboard/backlogs/backlogs_list.html'
    context_object_name = 'backlogs'

@login_required
class BacklogsDetailView(DetailView):
    model = Backlogs
    template_name = 'dashboard/backlogs/backlogs_detail.html'
    context_object_name = 'backlogs'

@login_required
class BacklogsCreateView(CreateView):
    model = Backlogs
    template_name = 'dashboard/backlogs/backlogs_form.html'
    fields = '__all__'
    success_url = reverse_lazy('backlogs_list')

@login_required
class BacklogsUpdateView(UpdateView):
    model = Backlogs
    template_name = 'dashboard/backlogs/backlogs_form.html'
    fields = '__all__'
    success_url = reverse_lazy('backlogs_list')

@login_required
class BacklogsDeleteView(DeleteView):
    model = Backlogs
    template_name = 'dashboard/backlogs/backlogs_confirm_delete.html'
    success_url = reverse_lazy('backlogs_list')

@login_required
class SupportMensagensListView(ListView):
    model = SupportMensagens
    template_name = 'dashboard/support/support_list.html'
    context_object_name = 'support'

@login_required
class SupportMensagensDetailView(DetailView):
    model = SupportMensagens
    template_name = 'dashboard/support/support_detail.html'
    context_object_name = 'support'

@login_required
class SupportMensagensCreateView(CreateView):
    model = SupportMensagens
    template_name = 'dashboard/support/support_form.html'
    fields = '__all__'
    success_url = reverse_lazy('support_list')

@login_required
class SupportMensagensUpdateView(UpdateView):
    model = SupportMensagens
    template_name = 'dashboard/support/support_form.html'
    fields = '__all__'
    success_url = reverse_lazy('support_list')

@login_required
class SupportMensagensDeleteView(DeleteView):
    model = SupportMensagens
    template_name = 'dashboard/support/support_confirm_delete.html'
    success_url = reverse_lazy('support_list')

@login_required
class UsuariosListView(ListView):
    model = Usuarios
    template_name = 'dashboard/usuarios/usuarios_list.html'
    context_object_name = 'usuarios'

@login_required
class UsuariosDetailView(DetailView):
    model = Usuarios
    template_name = 'dashboard/usuarios/usuarios_detail.html'
    context_object_name = 'usuarios'

@login_required
class UsuariosCreateView(CreateView):
    model = Usuarios
    template_name = 'dashboard/usuarios/usuarios_form.html'
    fields = '__all__'
    success_url = reverse_lazy('usuarios_list')

@login_required
class UsuariosUpdateView(UpdateView):
    model = Usuarios
    template_name = 'dashboard/usuarios/usuarios_form.html'
    fields = '__all__'
    success_url = reverse_lazy('usuarios_list')

@login_required
class UsuariosDeleteView(DeleteView):
    model = Usuarios
    template_name = 'dashboard/usuarios/usuarios_confirm_delete.html'
    success_url = reverse_lazy('usuarios_list')

