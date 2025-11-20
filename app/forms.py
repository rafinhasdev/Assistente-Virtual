from django import forms
from django.forms import ModelForm

from accounts.models import Usuarios
from Dashboard.models import Backlogs, SupportMensagens


class UsuarioForm(ModelForm):

    class Meta:
        model = Usuarios
        fields = "__all__"
        widgets = {
            "matricula": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "sobrenome": forms.TextInput(attrs={"class": "form-control"}),
            "numero": forms.TextInput(attrs={"class": "form-control"}),
        }


class SupporteForms(forms.ModelForm):
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
                'placeholder': 'Descreva aqui o ocorrido...',
            })
        }

class BacklogsForm(ModelForm):

    class Meta:
        model = Backlogs
        fields = "__all__"
        widgets = {
            "num_versao": forms.NumberInput(attrs={"class": "form-control"}),
            "data_postagem": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "data_alteracao": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "descricao": forms.TextInput(attrs={"class": "form-control"}),
            "dev_responsavel": forms.TextInput(attrs={"class": "form-control"}),
        }
