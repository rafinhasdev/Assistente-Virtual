from django.forms import ModelForm
from django import forms
from accounts.models import Usuarios
from .models import SupportReplyMensagens, SupportMensagens



class SupportReplyForms(forms.ModelForm):
    class Meta:
        model = SupportMensagens
        fields = ['descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={
                'style': (
                    'background: transparent;'
                    'color: white;'
                    'padding: 10px;'
                    'width: 100%;'
                    'height: 100%;'
                    'resize: none;'
                    'border: none;'
                    'outline: none;'
                ),
                'placeholder': 'Descreva aqui a resposta...',
            })
        }