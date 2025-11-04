from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuarios(AbstractUser):
    matricula = models.CharField(max_length=14, unique=True, null=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    sobrenome = models.CharField(max_length=255, null=True, blank=True)
    numero = models.CharField(max_length=20, null=True, blank=True)
    data_cadastro = models.DateField(auto_now_add=True)
    data_ultimo_login = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"

    def is_admin(self):
        return self.groups.filter(name='ADMINISTRADOR').exists()

    def is_user_simples(self):
        return self.groups.filter(name='USUARIO_SIMPLES').exists()
