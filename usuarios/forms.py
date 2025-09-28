from django.forms import ModelForm
from .models import Usuarios
from django import forms


class UsuarioForm(ModelForm):

    class Meta:
        model = Usuarios
        fields = '__all__'
        widgets = {
            'matricula' : forms.TextInput(attrs={'class': 'form-control' }),
            'email' : forms.EmailInput(attrs={'class': 'form-control' }),
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'sobrenome' : forms.TextInput(attrs={'class': 'form-control' }),
            'numero': forms.TextInput(attrs={'class': 'form-control' })
        }
