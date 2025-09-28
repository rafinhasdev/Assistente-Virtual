import re
from social_core.backends.oauth import SuapOAuth2

class SuapOAuth2(SuapOAuth2):
    name = "suap"
    AUTHORIZATION_URL = "https://suap.ifrn.edu.br/o/authorize/"
    ACCESS_TOKEN_METHOD = "POST"
    ACCESS_TOKEN_URL = "https://suap.ifrn.edu.br/o/token/"
    ID_KEY = "user_id"
    RESPONSE_TYPE = "code"
    REDIRECT_STATE = True
    STATE_PARAMETER = True
    USER_DATA_URL = "https://suap.ifrn.edu.br/api/eu/"

    def user_data(self, access_token, *args, **kwargs):

        method = "GET"
        data = {"Scope": kwargs.get("response").get("scope")}
        headers = {"Authorization": f"Bearer {access_token}"}
        response = self.request(
            url=self.USER_DATA_URL,
            method=method,
            data=data,
            headers=headers).json()
        
        return response
