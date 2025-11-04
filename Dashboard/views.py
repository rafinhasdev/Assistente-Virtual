from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Backlogs, SupportMensagens, Usuarios
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



@login_required
def index(request):
    return render(request, 'dashboard/index.html')



class BacklogsListView(LoginRequiredMixin, ListView):
    model = Backlogs
    template_name = 'dashboard/backlogs/backlogs_list.html'
    context_object_name = 'backlogs'


class BacklogsDetailView(LoginRequiredMixin, DetailView):
    model = Backlogs
    template_name = 'dashboard/backlogs/backlogs_detail.html'
    context_object_name = 'backlogs'


class BacklogsCreateView(LoginRequiredMixin, CreateView):
    model = Backlogs
    template_name = 'dashboard/backlogs/backlogs_form.html'
    fields = '__all__'
    success_url = reverse_lazy('backlogs_list')


class BacklogsUpdateView(LoginRequiredMixin, UpdateView):
    model = Backlogs
    template_name = 'dashboard/backlogs/backlogs_form.html'
    fields = '__all__'
    success_url = reverse_lazy('backlogs_list')

class BacklogsDeleteView(LoginRequiredMixin, DeleteView):
    model = Backlogs
    template_name = 'dashboard/backlogs/backlogs_confirm_delete.html'
    success_url = reverse_lazy('backlogs_list')

class SupportMensagensListView(LoginRequiredMixin, ListView):
    model = SupportMensagens
    template_name = 'dashboard/support/support_list.html'
    context_object_name = 'support'

class SupportMensagensDetailView(LoginRequiredMixin, DetailView):
    model = SupportMensagens
    template_name = 'dashboard/support/support_detail.html'
    context_object_name = 'support'

class SupportMensagensCreateView(LoginRequiredMixin, CreateView):
    model = SupportMensagens
    template_name = 'dashboard/support/support_form.html'
    fields = '__all__'
    success_url = reverse_lazy('support_list')

class SupportMensagensUpdateView(LoginRequiredMixin, UpdateView):
    model = SupportMensagens
    template_name = 'dashboard/support/support_form.html'
    fields = '__all__'
    success_url = reverse_lazy('support_list')

class SupportMensagensDeleteView(LoginRequiredMixin, DeleteView):
    model = SupportMensagens
    template_name = 'dashboard/support/support_confirm_delete.html'
    success_url = reverse_lazy('support_list')

class UsuariosListView(LoginRequiredMixin, ListView):
    model = Usuarios
    template_name = 'dashboard/usuarios/usuarios_list.html'
    context_object_name = 'usuarios'

class UsuariosDetailView(LoginRequiredMixin, DetailView):
    model = Usuarios
    template_name = 'dashboard/usuarios/usuarios_detail.html'
    context_object_name = 'usuarios'

class UsuariosCreateView(LoginRequiredMixin, CreateView):
    model = Usuarios
    template_name = 'dashboard/usuarios/usuarios_form.html'
    fields = '__all__'
    success_url = reverse_lazy('usuarios_list')

class UsuariosUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuarios
    template_name = 'dashboard/usuarios/usuarios_form.html'
    fields = '__all__'
    success_url = reverse_lazy('usuarios_list')

class UsuariosDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuarios
    template_name = 'dashboard/usuarios/usuarios_confirm_delete.html'
    success_url = reverse_lazy('usuarios_list')

