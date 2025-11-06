# SUAP/pipeline/save_user.py

from accounts.models import Usuarios
import logging

logger = logging.getLogger(__name__)

def save_suap_user(strategy, details, response, backend, *args, **kwargs):
    if backend.name != "suap":
        return {}

    suap_id = response.get("identificacao")

    first_name = response.get("primeiro_nome", "") or response.get("nome", "").split()[0]
    last_name = response.get("ultimo_nome", "") or (
        response.get("nome", "").split()[-1] if len(response.get("nome", "").split()) > 1 else ""
    )

    email = (
        response.get("email_preferencial")
        or response.get("email")
        or response.get("email_academico")
        or ""
    )

    username = suap_id

    # Verifica se já existe
    user = Usuarios.objects.filter(username=username).first()

    if user:
        # ✅ Apenas atualiza os dados, sem criar novo
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save(update_fields=["first_name", "last_name", "email"])
        created = False
    else:
        # ✅ Cria apenas uma vez
        user = Usuarios.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        created = True
    

    logger.info(f"{'Criado' if created else 'Atualizado'} usuário {user.username}")
    
    return {
        "is_new": created,
        "user": user,
        "username": user.username,
        "details": {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        }

        
    }



