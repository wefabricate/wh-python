import asyncio
from keycloak import KeycloakOpenID  # install with pip install python-keycloak
from weheat.abstractions.heat_pump import HeatPump
from weheat.abstractions.auth import WEHEAT_AUTH_URL, WEHEAT_API_URL, WEHEAT_REALM_NAME

# client ID and secret provided by Weheat
client_id = ''
client_secret = ''

# username and password used for the online portal
username = ''
password = ''

# your heat pump UUID
my_heat_pump_id = ''


async def demo():
    # login into keycloak and get an access token
    keycloak_open_id = KeycloakOpenID(server_url=WEHEAT_AUTH_URL,
                                      client_id=client_id,
                                      realm_name=WEHEAT_REALM_NAME,
                                      client_secret_key=client_secret)

    token_response = keycloak_open_id.token(username, password)
    # The access token is valid for its lifetime even after logging out
    keycloak_open_id.logout(token_response['refresh_token'])

    # construct the heat pump object and fetch its data
    hp = HeatPump(api_url=WEHEAT_API_URL, uuid=my_heat_pump_id)
    await hp.async_get_status(token_response['access_token'])

    # Print some of the information, look in the files for all available properties
    print(f'Heat pump status: {hp.heat_pump_state}')
    print(f'Heat pump RPM: {hp.compressor_percentage}%')
    print(f'Total produced central heating energy: {hp.energy_out_heating} kWh')

asyncio.run(demo())