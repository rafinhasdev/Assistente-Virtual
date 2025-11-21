import logging
from django.contrib.auth.models import Group
from accounts.models import Usuarios

logger = logging.getLogger(__name__)


def save_suap_user(strategy, details, response, backend, *args, **kwargs):
    if backend.name != "suap":
        return {}

    suap_id = response.get("identificacao")

    first_name = (
        response.get("primeiro_nome", "") or response.get("nome", "").split()[0]
    )
    last_name = response.get("ultimo_nome", "") or (
        response.get("nome", "").split()[-1]
        if len(response.get("nome", "").split()) > 1
        else ""
    )

    email = (
        response.get("email_preferencial")
        or response.get("email")
        or response.get("email_academico")
        or ""
    )

    username = suap_id
    default_password = f"IFRN{username}"
    user = Usuarios.objects.filter(username=username).first()
    

    if user:
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save(update_fields=["first_name", "last_name", "email"])
        created = False
    else:
        user = Usuarios.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        user.set_password(default_password)
        user.save()

        created = True
    
    try: 
        grupo_simples = Group.objects.get(name="USUARIO_SIMPLES")
        user.groups.add(grupo_simples)
    except:
        logger.error("Grupo inexistente ou falha em adicionar-lo")


    logger.info(f"{'Criado' if created else 'Atualizado'} usuário {user.username}")

    return {
        "is_new": created,
        "user": user,
        "username": user.username,
        "details": {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        },
    }
