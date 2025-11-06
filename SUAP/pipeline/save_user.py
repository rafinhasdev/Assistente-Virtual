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
    email = response.get("email_preferencial") or response.get("email") or ""

    username = suap_id
    numero = "" 

    user, created = Usuarios.objects.get_or_create(
        username=username,
        defaults={
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "numero": numero,
        }
    )

    return {"is_new": created, "user": user}
