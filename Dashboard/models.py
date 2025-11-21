from django.db import models

from accounts.models import Usuarios


class Backlogs(models.Model):
    num_versao = models.FloatField(unique=True, null=True)
    data_postagem = models.DateField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now_add=False)
    descricao = models.TextField(null=False, blank=False)
    dev_responsavel = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f"Versionamento: {self.num_versao}::{self.data_alteracao}"


class SupportMensagens(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True)
    descricao = models.TextField(null=True)
    data_envio = models.DateTimeField(auto_now_add=True, null=True)
    ativo = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return f"{self.usuario.nome}: {self.data_envio}"


class SupportReplyMensagens(models.Model):
    support = models.ForeignKey(SupportMensagens, on_delete=models.CASCADE, null=True)
    descricao = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    dev_responsavel = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f"{self.support.usuario.nome}: {self.data_envio}"
