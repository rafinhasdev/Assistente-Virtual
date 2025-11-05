from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser

class Usuarios(AbstractUser):
    matricula = models.CharField(max_length=14, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=False) 
    numero = models.CharField(max_length=20, null=True, blank=True)
    data_cadastro = models.DateTimeField(default=now, null=False, blank=False)
    data_ultimo_login = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.matricula})"

    def is_admin(self):
        return self.groups.filter(name='ADMINISTRADOR').exists()

    def is_user_simples(self):
        return self.groups.filter(name='USUARIO_SIMPLES').exists()
