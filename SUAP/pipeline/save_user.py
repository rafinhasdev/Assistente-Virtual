from django.utils import timezone
from app.models import Usuarios, Credenciais

def save_suap_user(strategy, details, user=None, response=None, *args, **kwargs):
    """
    Salva/atualiza o usuário e suas credenciais no banco de dados.
    """
    if not response:
        return

    matricula = response.get('identificacao') 
    nome = response.get('primeiro_nome') 
    sobrenome = response.get('ultimo_nome') 
    email = response.get('email_segundario') 
    numero = response.get('telefone') or '---'
    token = response.get('access_token') 

    usuario, created = Usuarios.objects.update_or_create(
        matricula=matricula,
        defaults={
            'email': email,
            'nome': nome,
            'sobrenome': sobrenome,
            'numero': numero,
            'data_cadastro': timezone.now(),
            'data_ultimo_login': timezone.now()
        }
    )

    Credenciais.objects.update_or_create(
        usuario=usuario,
        defaults={'suap_TOKEN': token}
    )

    return {'usuario': usuario}