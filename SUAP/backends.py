from social_core.backends.oauth import BaseOAuth2
import requests

class SuapOAuth2(BaseOAuth2):
    name = "suap"
    AUTHORIZATION_URL = "https://suap.ifrn.edu.br/o/authorize/"
    ACCESS_TOKEN_URL = "https://suap.ifrn.edu.br/o/token/"
    ACCESS_TOKEN_METHOD = "POST"
    USER_DATA_URL = "https://suap.ifrn.edu.br/api/rh/eu/"
    RESPONSE_TYPE = "code"
    REDIRECT_STATE = True
    STATE_PARAMETER = True
    ID_KEY = "identificacao"

    def get_user_details(self, response):
        return {
            'username': response.get('identificacao', ''),
            'email': response.get('email_preferencial') or response.get('email') or '',
            'first_name': response.get('primeiro_nome', ''),
            'last_name': response.get('ultimo_nome', ''),
        }

    def user_data(self, access_token, *args, **kwargs):
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(self.USER_DATA_URL, headers=headers)
        response.raise_for_status()
        data = response.json()
        data['access_token'] = access_token
        return data
