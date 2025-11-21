from django import forms
from .models import SupportMensagens, Backlogs


class BacklogsForm(forms.ModelForm):
    class Meta:
        model = Backlogs
        fields = ["num_versao", "data_alteracao", "descricao", "dev_responsavel"]

        base_style = (
            "background-color: #23313e;"
            "color: white;"
            "padding: 10px 12px;"
            "width: 100%;"
            "border: 1px solid #4b5563;"
            "border-radius: 8px;"
            "outline: none;"
            "font-size: 14px;"
        )

        widgets = {
            "num_versao": forms.NumberInput(
                attrs={"step": "0.1", "placeholder": "Ex: 1.1", "style": base_style}
            ),
            "data_alteracao": forms.DateTimeInput(
                attrs={"type": "datetime-local", "style": base_style}
            ),
            "descricao": forms.Textarea(
                attrs={
                    "placeholder": "Descreva as alterações realizadas...",
                    "rows": 4,
                    "style": base_style + "resize: none;",
                }
            ),
            "dev_responsavel": forms.TextInput(
                attrs={
                    "placeholder": "Nome do desenvolvedor responsável",
                    "style": base_style,
                }
            ),
        }

        labels = {
            "num_versao": "Versionamento",
            "data_alteracao": "Data da Alteração",
            "descricao": "Descrição",
            "dev_responsavel": "Dev responsável",
        }


class SupportReplyForms(forms.ModelForm):
    class Meta:
        model = SupportMensagens
        fields = ["descricao"]
        widgets = {
            "descricao": forms.Textarea(
                attrs={
                    "style": (
                        "background: transparent;"
                        "color: white;"
                        "padding: 10px;"
                        "width: 100%;"
                        "height: 100%;"
                        "resize: none;"
                        "border: none;"
                        "outline: none;"
                    ),
                    "placeholder": "Descreva aqui a resposta...",
                }
            )
        }
