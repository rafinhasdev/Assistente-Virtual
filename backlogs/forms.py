from django.forms import ModelForm
from django import forms
from .models import Backlogs



class BacklogsForm(ModelForm):

    class Meta:
        model = Backlogs
        fields = '__all__'
        widgets = {
            'num_versao' : forms.NumberInput(attrs={'class': 'form-control' }),
            'data_postagem' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_alteracao' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'descricao' : forms.TextInput(attrs={'class': 'form-control' }),
            'dev_responsavel' : forms.TextInput(attrs={'class': 'form-control' }),
        }