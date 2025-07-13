from django.db import models


class Usuarios(models.Model):
    matricula = models.CharField(max_length=14, unique=True, null=True)
    email = models.EmailField(unique=True, null=True)
    nome = models.CharField(max_length=255, null=True)
    sobrenome = models.CharField(max_length=255, null=False, blank=False)
    numero = models.CharField(max_length=20, null=False)
    data_cadastro = models.DateField(auto_now_add=True, null=True)
    data_ultimo_login = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.nome

class Backlogs(models.Model):
    num_versao = models.IntegerField(unique=True, null=True)
    data_postagem = models.DateField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now_add=False)
    descricao = models.TextField(null=False, blank=False)
    dev_responsavel = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f"Versionamento: {self.num_versao}::{self.data_alteracao}"

class Waha(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True)
    num_sessao = models.CharField(max_length=255, null=True, unique=True)
    data_ultima_alteracao = models.DateField(auto_now_add=True)
    token_api_suap = models.CharField(max_length=255, unique=True, null=True)

    def __str__(self):
        return f"Sessão: {self.num_sessao}"