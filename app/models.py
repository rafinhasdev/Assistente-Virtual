from django.db import models

class Usuarios(models.Model):
    matricula = models.CharField(max_length=14, unique=True, null=True)
    nome = models.CharField(max_length=255, null=True)
    sobrenome = models.CharField(max_length=255, null=False, blank=False)
    data_cadastro = models.DateField(auto_now_add=True, null=True)
    data_ultimo_login = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.nome

class Backlogs(models.Model):
    num_versao = models.IntegerField(max_length=20, unique=True, null=True)
    data_postagem = models.DateField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(null=False, blank=False)

    def __str__(self) -> str:
        return f"Versionamento: {self.num_versao}::{self.data_alteracao}"

class Waha (models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True)
    num_sessao = models.CharField(max_length=255, null=True, unique=True)
    numero = models.CharField(max_length=20, null=True, unique=True)
    ultima_alteracao = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Sessão: {self.num_sessao}"