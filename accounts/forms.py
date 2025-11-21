from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Usuarios

class UsuariosForm(UserCreationForm):
    class meta:
        model = Usuarios
        fields = ["username", "email", "numero", "first_name", "last_name"]

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
            "username": forms.TextInput(
                attrs={"placeholder": "Nome de usuário", "style": base_style}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "E-mail", "style": base_style}
            ),
            "numero": forms.TextInput(
                attrs={"placeholder": "Número", "style": base_style}
            ),
            "first_name": forms.TextInput(
                attrs={"placeholder": "Nome", "style": base_style}
            ),
            "last_name": forms.TextInput(
                attrs={"placeholder": "Sobrenome", "style": base_style}
            ),
        }
