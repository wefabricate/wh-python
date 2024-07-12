# Weheat backend client

This is a client for the Weheat backend. It is automatically generated from the OpenAPI specification.

## Requirements.

Python 3.7+

## Installation & Usage

You can install directly using:

```sh
pip install weheat
```

Then import the package:

```python
import weheat
```



## Getting Started

After installation, you can now use the client to interact with the Weheat backend.

```python
import datetime
from keycloak import KeycloakOpenID  # install with pip install python-keycloak
from weheat import ApiClient, Configuration, HeatPumpApi, HeatPumpLogApi, EnergyLogApi

# input your information here
auth_url = 'https://auth.weheat.nl/auth/'
api_url = 'https://api.weheat.nl'
realm_name = 'Weheat'
my_client_id = 'WeheatCommunityAPI'  # client ID and secret provided by Weheat
my_client_secret = ''
username = ''  # username and password used for the online portal
password = ''
my_heat_pump_id = ''  # your heat pump UUID

# Get the access token from keycloak
keycloak_open_id = KeycloakOpenID(server_url=auth_url,
                                  client_id=my_client_id,
                                  realm_name=realm_name,
                                  client_secret_key=my_client_secret)

token_response = keycloak_open_id.token(username, password)
keycloak_open_id.logout(token_response['refresh_token'])

# Create the cinfiguration object
config = Configuration(host=api_url, access_token=token_response['access_token'])

# with the client the APIs can be accessed
with ApiClient(configuration=config) as client:
    # Getting all heat pumps that the user has access to
    response = HeatPumpApi(client).api_v1_heat_pumps_get_with_http_info()

    if response.status_code == 200:
        print(f'My heat pump: {response.data}')

    # Getting the latest log of the heat pump
    response = HeatPumpLogApi(client).api_v1_heat_pumps_heat_pump_id_logs_latest_get_with_http_info(
        heat_pump_id=my_heat_pump_id)

    if response.status_code == 200:
        print(f'My heat pump logs: {response.data}')

    # Getting the energy logs of the heat pump in a specific period
    # interval can be  "Minute", "FiveMinute", "FifteenMinute", "Hour", "Day", "Week", "Month", "Year"
    response = EnergyLogApi(client).api_v1_energy_logs_heat_pump_id_get_with_http_info(heat_pump_id=my_heat_pump_id,
                                                                                       start_time=datetime.datetime(
                                                                                           2024, 6,
                                                                                           22, 0, 0,
                                                                                           0),
                                                                                       end_time=datetime.datetime(2024,
                                                                                                                  6, 22,
                                                                                                                  15, 0,
                                                                                                                  0),
                                                                                       interval='Hour')

    if response.status_code == 200:
        print(f'My energy logs: {response.data}')


```



