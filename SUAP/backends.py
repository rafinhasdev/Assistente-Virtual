import re
from social_core.backends.oauth import BaseOAuth2


class SuapOAuth2(BaseOAuth2):
    name = "suap"
    AUTHORIZATION_URL = "https://suap.ifrn.edu.br/o/authorize/"
    ACCESS_TOKEN_METHOD = "POST"
    ACCESS_TOKEN_URL = "https://suap.ifrn.edu.br/o/token/"
    ID_KEY = "identificacao"
    RESPONSE_TYPE = "code"
    REDIRECT_STATE = True
    STATE_PARAMETER = True
    USER_DATA_URL = "https://suap.ifrn.edu.br/api/eu/"
    EXTRA_USER_DATA_URL = (
        "https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/"
    )

    def user_data(self, access_token, *args, **kwargs):
        method = "GET"
        data = {"scope": kwargs.get("response").get("scope")}
        headers = {"Authorization": f"Bearer {access_token}"}
        response = self.request(
            url=self.USER_DATA_URL, method=method, data=data, headers=headers
        ).json()

        extra_data = self.request(
            url=self.EXTRA_USER_DATA_URL, method=method, data=data, headers=headers
        ).json()

        response.update({"cpf": extra_data.get("cpf", "")})
        return response

    def get_user_details(self, response):
        nome = response.get("nome", "")
        partes = nome.split()
        first_name = partes[0] if partes else ""
        last_name = partes[-1] if len(partes) > 1 else ""

        username = f"{first_name.lower()}_{response.get(self.ID_KEY)}"

        return {
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "email": response.get("email", ""),
        }
