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
        """
        Apenas mapeia os campos do response para os dados do usuário.
        """
        return {
            'username': response.get('username', response.get('identificacao', '')),
            'email': response.get('email_segundario', ''),
            'first_name': response.get('primeiro_nome', ''),
            'last_name': response.get('ultimo_nome', '---'),
        }

    def user_data(self, access_token, *args, **kwargs):
        """
        Busca os dados do usuário via API do SUAP.
        """
        import requests
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(self.USER_DATA_URL, headers=headers)
        response.raise_for_status()
        data = response.json()
        # Inclui o token para usar no pipeline
        data['access_token'] = access_token
        return data