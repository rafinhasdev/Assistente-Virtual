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
# Create your models here.
