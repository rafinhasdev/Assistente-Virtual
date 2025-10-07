from social_core.backends.oauth import BaseOAuth2

class SuapOAuth2(BaseOAuth2):
    """Backend OAuth2 para autenticação via SUAP."""
    name = "suap"
    AUTHORIZATION_URL = "https://suap.ifrn.edu.br/o/authorize/"
    ACCESS_TOKEN_METHOD = "POST"
    ACCESS_TOKEN_URL = "https://suap.ifrn.edu.br/o/token/"
    ID_KEY = "user_id"
    RESPONSE_TYPE = "code"
    REDIRECT_STATE = True
    STATE_PARAMETER = True
    USER_DATA_URL = "https://suap.ifrn.edu.br/api/eu/"

    def get_user_details(self, response):
        """Extrai os detalhes do usuário da resposta do SUAP."""
        return {
            'email': response.get('email'),
        }

    def user_data(self, access_token, *args, **kwargs):
        """Obtém dados do usuário a partir do token."""
        import requests
        response = requests.get(
            'https://suap.ifrn.edu.br/api/eu/',
            headers={'Authorization': f'Bearer {access_token}'}
        )
        return response.json()