from django.db import models
from usuarios.models import Usuarios


class SupportMensagens(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=True)
    descricao = models.TextField(null=True)
    data_envio = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return f"{self.usuario.nome}: {self.data_envio}"
# Create your models here.
