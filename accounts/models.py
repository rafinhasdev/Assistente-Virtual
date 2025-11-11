from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class Usuarios(AbstractUser):
    username = models.CharField(
        max_length=150, verbose_name="Usuário", null=True, blank=True
    )
    email = models.EmailField(
        verbose_name="E-mail", max_length=255, null=True, blank=True
    )
    numero = models.CharField(
        verbose_name="Numero", max_length=20, null=True, blank=True
    )
    first_name = models.CharField(
        verbose_name="Nome", max_length=255, null=True, blank=True
    )
    last_name = models.CharField(
        verbose_name="Sobrenome", max_length=255, null=True, blank=True
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    def is_admin(self):
        return self.groups.filter(name="ADMINISTRADOR").exists()

    def is_user_simples(self):
        return self.groups.filter(name="USUARIO_SIMPLES").exists()
