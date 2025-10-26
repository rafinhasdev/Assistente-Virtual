from django.db import models
from app.models import Usuarios

class Credenciais(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True)
    suap_token = models.CharField(max_length=255)
    bearer = models.CharField(max_length=255)


    def __str__(self):
        return f"Token: {self.usuario.nome}, Login: {self.usuario.data_ultimo_login}"
    