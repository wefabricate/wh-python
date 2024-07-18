from dataclasses import dataclass

from weheat.configuration import Configuration
from weheat.api_client import ApiClient
from weheat.api.heat_pump_api import HeatPumpApi


class HeatPumpDiscovery:
    @dataclass
    class HeatPumpInfo:
        uuid: str
        name: str
        model: str
        sn : str
        has_dhw: bool = False

    @staticmethod
    def discover(api_url: str, access_token: str) -> list[HeatPumpInfo]:
        discovered_pumps = []

        config = Configuration(host=api_url, access_token=access_token)

        with ApiClient(configuration=config) as client:
            # try:
            response = HeatPumpApi(client).api_v1_heat_pumps_get_with_http_info()
            if response.status_code == 200:
                for pump in response.data:
                    model_string = "BlackBird P80 heat pump"
                    if pump.model == 1:
                        model_string = "BlackBird P60 heat pump"
                    elif pump.model == 2:
                        model_string = "Sparrow P60 heat pump"

                    dhw = False
                    if pump.dhw_type is not None and pump.dhw_type == 1:
                        dhw = True

                    discovered_pumps.append(
                        HeatPumpDiscovery.HeatPumpInfo(
                            uuid=pump.id,
                            name=pump.name,
                            model=model_string,
                            sn=pump.serial_number,
                            has_dhw=dhw,
                        )
                    )
        return discovered_pumps