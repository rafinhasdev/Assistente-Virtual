from django.forms import ModelForm
from django import forms
from .models import Backlogs
from usuarios.models import Usuarios
from support.models import SupportMensagens



class SupporteForms(ModelForm):

    usuario = forms.ModelChoiceField(
        queryset=Usuarios.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = SupportMensagens
        fields = ['usuario', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }
