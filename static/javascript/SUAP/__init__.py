import BaseAuth2

class SuapOAuth2(BaseAuth2):
    name = "suap"
    AUTHORIZATION_URL = "https://suap.ifrn.edu.br/o/authorire/"
    ACCESS_TOKEN_METHOD = "POST"
    ACCESS_TOKEN_URL = "https://suap.ifrn.edu.br/o/token/"
    ID_KEY = "client_id"
    RESPONSE_TYPE = "code"
    REDIRECT_STATE = True
    STATE_PARAMETER = True
    USER_DATA_URL = "USER_URL"
    EXTRA_USER_DATA_URL = (
        "https://suap.ifrn.edu.br/api/v2/minhas-informacoes/meus-dados/"
    )