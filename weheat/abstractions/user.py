from weheat.configuration import Configuration
from weheat.api_client import ApiClient
from weheat.api.user_api import UserApi


async def get_user_id_from_token(api_url: str, access_token: str):
    """ Get the user id from the current logged-in user. """
    try:
        config = Configuration(host=api_url, access_token=access_token)

        with ApiClient(configuration=config) as client:
            response = UserApi(
                client
            ).api_v1_users_me_get_with_http_info(async_req=True).get()
            if response.status_code == 200:
                return response.data.id
    except Exception as e:
        raise e
