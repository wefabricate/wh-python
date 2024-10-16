"""Weheat heat pump abstraction from the API."""
from enum import Enum, auto
from weheat.configuration import Configuration
from weheat.api_client import ApiClient
from weheat.api.heat_pump_log_api import HeatPumpLogApi
from weheat.api.energy_log_api import EnergyLogApi
from datetime import datetime, timedelta

# before this date no energy logs are available, so start from this point onwards
START_DATE = datetime(2023, 1, 1, 0, 0, 0)


class HeatPump:
    """Heat pump class representing a heat pump."""
    class State(Enum):
        STANDBY = auto()
        WATER_CHECK = auto()
        HEATING = auto()
        COOLING = auto()
        DHW = auto()
        LEGIONELLA_PREVENTION = auto()
        DEFROSTING = auto()
        SELF_TEST = auto()
        MANUAL_CONTROL = auto()

    def __init__(self, api_url: str, uuid: str) -> None:
        self._api_url = api_url
        self._uuid = uuid
        self._last_log = None
        self._energy_consumption = None

    def get_status(self, access_token: str):
        """Updates the heat pump instance with data from the API."""
        try:
            config = Configuration(host=self._api_url, access_token=access_token)

            with ApiClient(configuration=config) as client:
                response = HeatPumpLogApi(
                    client
                ).api_v1_heat_pumps_heat_pump_id_logs_latest_get_with_http_info(
                    heat_pump_id=self._uuid
                )
                if response.status_code == 200:
                    self._last_log = response.data

                # Also get all energy totals form past years and add them together
                # As end time pick today + 1 day to avoid issues with timezones
                response = EnergyLogApi(client).api_v1_energy_logs_heat_pump_id_get_with_http_info(heat_pump_id=self._uuid,
                                                                                start_time=START_DATE,
                                                                                end_time=datetime.now() + timedelta(days=1),
                                                                                interval='Year')

                if response.status_code == 200:
                    # aggregate the energy consumption
                    self._energy_consumption = 0
                    for year in response.data:
                        self._energy_consumption += year.total_ein_cooling
                        self._energy_consumption += year.total_ein_heating
                        self._energy_consumption += year.total_ein_heating_defrost
                        self._energy_consumption += year.total_ein_dhw
                        self._energy_consumption += year.total_ein_dhw_defrost



        except Exception as e:
            self._last_log = None
            self._energy_consumption = None
            raise e

    def _if_available(self, key):
        """Returns the value from the last logged value if available. None otherwise."""
        if self._last_log is not None and hasattr(self._last_log, key):
            return getattr(self._last_log, key)
        return None

    def __str__(self):
        return f"WeheatHeatPump(uuid={self._uuid}, last update={self._if_available('timestamp')})"

    def __repr__(self):
        return self.__str__()

    @property
    def water_inlet_temperature(self):
        """The heat pump water inlet temperature."""
        return self._if_available("t_water_in")

    @property
    def water_outlet_temperature(self):
        """The heat pump water outlet temperature."""
        return self._if_available("t_water_out")

    @property
    def water_house_in_temperature(self):
        """The water house in temperature."""
        return self._if_available("t_water_house_in")

    @property
    def air_inlet_temperature(self):
        """The heat pump air inlet temperature."""
        return self._if_available("t_air_in")

    @property
    def air_outlet_temperature(self):
        """The heat pump air outlet temperature."""
        return self._if_available("t_air_out")

    @property
    def thermostat_water_setpoint(self):
        """The  thermostat water setpoint."""
        return self._if_available("t_thermostat_setpoint")

    @property
    def thermostat_room_temperature(self):
        """The thermostat current room temperature."""
        return self._if_available("t_room")

    @property
    def thermostat_room_temperature_setpoint(self):
        """The thermostat room temperature setpoint."""
        return self._if_available("t_room_target")

    @property
    def thermostat_on_off_state(self):
        """The thermostat on/off state."""
        return self._if_available("on_off_thermostat_state")

    @property
    def power_input(self):
        """The heat pumps power input."""
        return self._if_available("cm_mass_power_in")

    @property
    def power_output(self):
        """The heat pumps hydraulic output power."""
        return self._if_available("cm_mass_power_out")

    @property
    def dhw_top_temperature(self):
        """The DHW vessel top temperature."""
        return self._if_available("t1")

    @property
    def dhw_bottom_temperature(self):
        """The DHW vessel bottom temperature."""
        return self._if_available("t2")

    @property
    def cop(self):
        """
        Returns the coefficient of performance of the heat pump.
        Note that this is calculated from a singular log entry and might not be accurate when the
        heat pump is changing its output power or switching states
        """
        input = self.power_input
        output = self.power_output
        if input is not None and output is not None and input != 0:
            return output / input

    @property
    def inside_unit_water_pump_state(self):
        """Decoded water pump state."""
        return self._if_available("control_bridge_status_decoded_water_pump")

    @property
    def inside_unit_auxilary_pump_state(self):
        """Decoded auxilary pump state."""
        return self._if_available("control_bridge_status_decoded_water_pump2")

    @property
    def inside_unit_dhw_valve_or_pump_state(self):
        """Decoded DHW valve or pump state."""
        return self._if_available("control_bridge_status_decoded_dhw_valve")

    @property
    def inside_unit_gas_boiler_state(self):
        """Decoded gas boiler state."""
        return self._if_available("control_bridge_status_decoded_gas_boiler")

    @property
    def inside_unit_gas_electric_heater(self):
        """Decoded electric heater state."""
        return self._if_available("control_bridge_status_decoded_electric_heater")

    @property
    def compressor_rpm(self):
        """Compressor RPM."""
        return self._if_available("rpm")

    @property
    def heat_pump_state(self) -> State | None:
        """The heat pump state."""
        numeric_state = self._if_available("state")
        if numeric_state is None:
            return None

        if numeric_state == 40:
            return self.State.STANDBY
        elif numeric_state == 70:
            return self.State.HEATING
        elif numeric_state == 130:
            return self.State.COOLING
        elif numeric_state == 150:
            return self.State.DHW
        elif numeric_state == 160:
            return self.State.LEGIONELLA_PREVENTION
        elif numeric_state == 170:
            return self.State.SELF_TEST
        elif numeric_state == 180:
            return self.State.MANUAL_CONTROL
        elif numeric_state == 200:
            return self.State.DEFROSTING
        return None

    @property
    def energy_total(self):
        """The total used energy in kWh from 2023 to now."""
        return self._energy_consumption
