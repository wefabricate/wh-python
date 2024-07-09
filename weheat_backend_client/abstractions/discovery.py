from dataclasses import dataclass

from weheat_backend_client.configuration import Configuration
from weheat_backend_client.api_client import ApiClient
from weheat_backend_client.api.heat_pump_api import HeatPumpApi


class HeatPumpDiscovery:
    @dataclass
    class HeatPump:
        uuid: str
        name: str
        household_name: str

    @staticmethod
    def discover(api_url: str, access_token: str) -> list[HeatPump]:
        discovered_pumps = {}

        config = Configuration(host=api_url, access_token=access_token)

        with ApiClient(configuration=config) as client:
            # try:
            response = HeatPumpApi(client).api_v1_heat_pumps_get_with_http_info()
            if response.status_code == 200:
                for pump in response.data:
                    discovered_pumps[pump.id] = pump.serial_number

        return discovered_pumps