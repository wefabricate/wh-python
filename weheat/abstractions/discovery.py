import asyncio
from dataclasses import dataclass

from weheat import DeviceState
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
    async def async_discover_active(api_url: str, access_token: str) -> list[HeatPumpInfo]:
        discovered_pumps = []

        config = Configuration(host=api_url, access_token=access_token)

        with ApiClient(configuration=config) as client:

            response = HeatPumpApi(client).api_v1_heat_pumps_get_with_http_info('', 1, 1000, DeviceState.NUMBER_3 ,async_req=True)

            response = await asyncio.to_thread(response.get)

            if response.status_code == 200:
                for pump in response.data:
                    # Model of the heat pump
                    # - BlackBirdP80: BlackBird P80 heat pump (0)
                    # - BlackBirdP60: BlackBird P60 heat pump (1)
                    # - SparrowP60Brown: Sparrow P60 heat pump, colour brown (default) (2)
                    # - SparrowP60Green: Sparrow P60 heat pump, colour green (3)
                    # - SparrowP60Grey: Sparrow P60 heat pump, colour grey (4)
                    # - FlintP40: Flint P40 heat pump (5)
                    model_string = "Blackbird P80 heat pump"
                    if pump.model == 1:
                        model_string = "Blackbird P60 heat pump"
                    elif 2 <= pump.model <= 4:
                        model_string = "Sparrow P60 heat pump"
                    elif pump.model == 5:
                        model_string = "Flint P40 heat pump"


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