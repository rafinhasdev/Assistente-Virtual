from django.forms import ModelForm
from django import forms
from .models import Usuarios, SupportMensagens


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