from django.db import models

class Backlogs(models.Model):
    num_versao = models.FloatField(unique=True, null=True)
    data_postagem = models.DateField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now_add=False)
    descricao = models.TextField(null=False, blank=False)
    dev_responsavel = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f"Versionamento: {self.num_versao}::{self.data_alteracao}"
# Create your models here.
