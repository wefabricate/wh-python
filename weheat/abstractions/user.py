import asyncio

import aiohttp

from weheat.configuration import Configuration
from weheat.api_client import ApiClient
from weheat.api.user_api import UserApi


async def async_get_user_id_from_token(api_url: str, access_token: str, client_session:aiohttp.ClientSession|None = None):
    """ Get the user id from the current logged-in user. """
    try:
        config = Configuration(host=api_url, access_token=access_token, client_session=client_session)

        async with ApiClient(configuration=config) as client:
            response = await UserApi(
                client
            ).api_v1_users_me_get_with_http_info()

            if response.status_code == 200:
                return response.data.id
    except Exception as e:
        raise e
