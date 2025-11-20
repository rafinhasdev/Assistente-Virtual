from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django.db.models import Q
from .models import Backlogs, SupportMensagens, SupportReplyMensagens
from accounts.models import Usuarios




@login_required
def index(request):
    return render(request, "dashboard/index.html")


class BacklogsListView(LoginRequiredMixin, ListView):
    """
    View responsável por listar todos os Backlogs no dashboard.

    Permite a filtragem do queryset por:
    - Desenvolvedor responsável (`dev`)
    - Número da versão (`versao`)
    - Data mínima de postagem (`data_ini`)

    Attributes:
        model (Model): O modelo Django a ser usado (Backlogs).
        template_name (str): O caminho do template para renderização.
        context_object_name (str): O nome da variável de contexto para a lista de objetos.
        paginate_by (int): O número de itens por página.
    """
    model = Backlogs
    template_name = "dashboard/backlogs/backlogs_list.html"
    context_object_name = "backlogs"
    paginate_by = 10

    def get_queryset(self):
        """
        Retorna o queryset de Backlogs, aplicando filtros baseados em GET request.

        A listagem é ordenada pela data de postagem de forma decrescente.

        Returns:
            QuerySet: Um QuerySet filtrado e ordenado do modelo Backlogs.
        """
        queryset = super().get_queryset()

        filtro_dev = self.request.GET.get('dev')
        filtro_version = self.request.GET.get('versao')
        filtro_date = self.request.GET.get('data_ini')

        if filtro_dev:
            queryset = queryset.filter(dev_responsavel__icontains=filtro_dev)

        if filtro_version:
            filtro_version = float(filtro_version)
            queryset = queryset.filter(num_versao__exact=filtro_version)
        
        if filtro_date:
            queryset = queryset.filter(data_postagem__gte=filtro_date)
        
        return queryset.order_by('-data_postagem')

    def get_context_data(self, **kwargs):
        """
        Adiciona os valores dos filtros de busca atuais ao contexto.

        Esses valores são usados para preencher novamente os campos do formulário
        de busca no template após a filtragem.

        Returns:
            dict: O dicionário de contexto estendido.
        """
        context = super().get_context_data(**kwargs)

        context['filtro_dev'] = self.request.GET.get('dev', '') 
        context['filtro_versao'] = self.request.GET.get('versao', '')
        context['filtro_data_ini'] = self.request.GET.get('data_ini', '')

        return context
class BacklogsDetailView(LoginRequiredMixin, DetailView):
    model = Backlogs
    template_name = "dashboard/backlogs/backlogs_detail.html"
    context_object_name = "backlogs"


class BacklogsCreateView(LoginRequiredMixin, CreateView):
    model = Backlogs
    template_name = "dashboard/backlogs/backlogs_form.html"
    fields = "__all__"
    success_url = reverse_lazy("backlogs_list")


class BacklogsUpdateView(LoginRequiredMixin, UpdateView):
    model = Backlogs
    template_name = "dashboard/backlogs/backlogs_form.html"
    fields = "__all__"
    success_url = reverse_lazy("backlogs_list")


class BacklogsDeleteView(LoginRequiredMixin, DeleteView):
    model = Backlogs
    template_name = "dashboard/backlogs/backlogs_confirm_delete.html"
    success_url = reverse_lazy("backlogs_list")


class SupportMensagensListView(LoginRequiredMixin, ListView):
    """
    Lista todas as mensagens de suporte enviadas pelos usuários.

    Permite a filtragem por nome de usuário, data de envio e descrição.
    """
    model = SupportMensagens
    template_name = "dashboard/suporte/support_list.html"
    context_object_name = "support"
    paginate_by = 10

    def get_queryset(self):
        """
        Aplica filtros baseados em GET request (user, data_env, descricao)
        e ordena por data de envio.
        """
        queryset = super().get_queryset()

        filtro_user = self.request.GET.get('user')
        filtro_data = self.request.GET.get('data_env')
        filtro_desc = self.request.GET.get('descricao')

        if filtro_user:
            queryset = queryset.filter(usuario__username__icontains=filtro_user)
        
        if filtro_data:
            queryset = queryset.filter(data_envio__gte=filtro_data)
        
        if filtro_desc:
            queryset = queryset.filter(descricao__icontains=filtro_desc)

        return queryset.order_by('data_envio')
    def get_context_data(self, **kwargs):
        """Adiciona os valores dos filtros de busca ao contexto."""
        context = super().get_context_data(**kwargs)

        context['filtro_user'] = self.request.GET.get('user', '') 
        context['filtro_data'] = self.request.GET.get('data_env', '')
        context['filtro_desc'] = self.request.GET.get('descricao', '')

        return context
class SupportMensagensDetailView(LoginRequiredMixin, DetailView):
    model = SupportMensagens
    template_name = "dashboard/support/support_detail.html"
    context_object_name = "support"


class SupportMensagensCreateView(LoginRequiredMixin, CreateView):
    model = SupportMensagens
    template_name = "dashboard/suporte/support_form.html"
    fields = "__all__"
    success_url = reverse_lazy("support_list")


class SupportMensagensUpdateView(LoginRequiredMixin, UpdateView):
    model = SupportMensagens
    template_name = "dashboard/support/support_form.html"
    fields = "__all__"
    success_url = reverse_lazy("support_list")


class SupportMensagensDeleteView(LoginRequiredMixin, DeleteView):
    model = SupportMensagens
    template_name = "dashboard/support/support_confirm_delete.html"
    success_url = reverse_lazy("support_list")

class SupportMensagemReplyView(LoginRequiredMixin, View):
    template_name = "dashboard/suporte/support_reply.html"

    def get(self, request, pk):
        support = get_object_or_404(SupportMensagens, pk=pk)
        return render(request, self.template_name, {"support": support})

    def post(self, request, pk):
        support = get_object_or_404(SupportMensagens, pk=pk)
        resposta = request.POST.get("resposta")

        if not resposta:
            messages.error(request, "Você precisa escrever uma resposta.")
            return redirect("support_reply", pk=pk)

        SupportReplyMensagens.objects.create(
            support=support,
            descricao=resposta,
            dev_responsavel=request.user.username,  
        )

        email = EmailMultiAlternatives(
            subject="Resposta ao seu pedido de suporte",
            body=resposta,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[support.usuario.email],
        )

        email.attach_alternative(f"""
        <p>Olá <strong>{support.usuario.first_name}</strong>,</p>
        <p>{resposta}</p>
        <p>Atenciosamente,<br>Assitente Felipe</p>
        """, "text/html")

        email.send()

        support.ativo = False
        support.save()

        messages.success(request, "Resposta enviada e registrada com sucesso!")
        return redirect("support_list")



class UsuariosListView(LoginRequiredMixin, ListView):
    """
    Lista todos os usuários registrados no sistema.

    Permite a busca por nome/sobrenome e filtragem por username ou email.
    """
    model = Usuarios
    template_name = "dashboard/usuarios/usuarios_list.html"
    context_object_name = "usuarios"
    paginate_by = 10

    def get_queryset(self):
        """
        Filtra os usuários por termo de busca (first_name/last_name),
        username específico ou email.
        """
        queryset = super().get_queryset()

        termo_busca = self.request.GET.get('q')
        filtro_username = self.request.GET.get('username')
        filtro_email = self.request.GET.get('email')

        if termo_busca:
            queryset = queryset.filter(
                Q(first_name__icontains = termo_busca) | Q(last_name__icontains = termo_busca)
            )
        if filtro_username:
            queryset = queryset.filter(username__icontains=filtro_username)

        if filtro_email:
            queryset = queryset.filter(email__icontains=filtro_email)

        return queryset.order_by('username')
    
    def get_context_data(self, **kwargs):
        """Adiciona os termos de busca e filtros atuais ao contexto."""
        context = super().get_context_data(**kwargs)
    
        context['termo_busca'] = self.request.GET.get('q', '') 
        context['filtro_username'] = self.request.GET.get('username', '')
        context['filtro_email'] = self.request.GET.get('email', '')

        return context
class UsuariosDetailView(LoginRequiredMixin, DetailView):
    model = Usuarios
    template_name = "dashboard/usuarios/usuarios_detail.html"
    context_object_name = "usuarios"


class UsuariosCreateView(LoginRequiredMixin, CreateView):
    model = Usuarios
    template_name = "dashboard/usuarios/usuarios_form.html"
    fields = "__all__"
    success_url = reverse_lazy("usuarios_list")


class UsuariosUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuarios
    template_name = "dashboard/usuarios/usuarios_form.html"
    fields = "__all__"
    success_url = reverse_lazy("usuarios_list")


class UsuariosDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuarios
    template_name = "dashboard/usuarios/usuarios_confirm_delete.html"
    success_url = reverse_lazy("usuarios_list")
