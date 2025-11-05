from django.contrib.auth import get_user_model

User = get_user_model()

def save_suap_user(backend, user, response, *args, **kwargs):
    # Dados que vêm do SUAP
    matricula = response.get("matricula") or response.get("username")
    nome = response.get("nome")
    email = response.get("email")

    if not matricula:  # Segurança extra
        return

    # 1. Verifica se o usuário já existe
    try:
        user = User.objects.get(username=matricula)
        return {"is_new": False, "user": user}
    except User.DoesNotExist:
        pass

    # 2. Se não existir, cria um novo
    user = User.objects.create_user(
        username=matricula,  # agora username = matrícula
        email=email,
        first_name=nome.split()[0] if nome else "",
        last_name=" ".join(nome.split()[1:]) if nome else "",
        password=None  # autenticação social não usa senha
    )

    return {"is_new": True, "user": user}

