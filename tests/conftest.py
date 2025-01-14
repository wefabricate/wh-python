import pytest
from dataclasses import dataclass
from keycloak import KeycloakOpenID

asyncio_default_fixture_loop_scope = "function"

def pytest_addoption(parser):
    # These are used by the STK500 interface

    parser.addoption(
        "--api_url",
        action="store",
        type=str,
        help="API url",
        required=True,
    )
    parser.addoption(
        "--auth_url",
        action="store",
        type=str,
        help="Authentication url",
        required=True,
    )
    parser.addoption(
        "--client_id",
        action="store",
        type=str,
        help="Client id",
        required=True,
    )
    parser.addoption(
        "--client_secret",
        action="store",
        type=str,
        help="Client secret",
        required=True,
    )
    parser.addoption(
        "--user",
        action="store",
        type=str,
        help="User email",
        required=True,
    )
    parser.addoption(
        "--password",
        action="store",
        type=str,
        help="User password",
        required=True,
    )





@dataclass
class ApiInfo:
    api_url: str
    auth_url: str
    client_id: str
    client_secret: str
    user: str
    password: str
    access_token: str


@pytest.fixture()
def api_fixture(request):
    api_info = ApiInfo(request.config.getoption('--api_url'), request.config.getoption('--auth_url'),
                       request.config.getoption('--client_id'), request.config.getoption('--client_secret'),
                       request.config.getoption('--user'), request.config.getoption('--password'), "")

    print(f"Logging in for {api_info.user} at {api_info.auth_url}")
    try:
        keycloak_open_id = KeycloakOpenID(server_url=api_info.auth_url, client_id=api_info.client_id,
                                          realm_name="Weheat",
                                          client_secret_key=api_info.client_secret)

        token_response = keycloak_open_id.token(api_info.user, api_info.password)
        keycloak_open_id.logout(token_response['refresh_token'])

        api_info.access_token = token_response['access_token']
    except Exception as e:
        print(f'Failed to authenticate: {e}')

    print(f'Access token received')

    return api_info


