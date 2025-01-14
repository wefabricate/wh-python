import pytest
from pydantic import ValidationError

from weheat.abstractions.heat_pump import HeatPump

from weheat.abstractions.discovery import HeatPumpDiscovery
from weheat.abstractions.user import async_get_user_id_from_token
from weheat.exceptions import UnauthorizedException, ForbiddenException


uuid_list = [
    '54ad613f-48e5-4583-b0e0-1a96d29131fa',
    '306625f3-124a-42eb-8e31-952963c65932',
    '573852f6-029f-4106-a019-2183b14a351f'
]

@pytest.mark.asyncio
async def test_discovery(api_fixture):
    discovery = await HeatPumpDiscovery.async_discover_active(api_url=api_fixture.api_url, access_token=api_fixture.access_token)

    #The account is configured to find at least one Blackbird, one sparrow and one flint
    assert len(discovery) >= 3

    #check some information for each pump, find it by type in the list
    blackbird = [hp for hp in discovery if 'blackbird' in hp.model.lower()]
    sparrow = [hp for hp in discovery if 'sparrow' in hp.model.lower()]
    flint = [hp for hp in discovery if 'flint' in hp.model.lower()]

    # sanity check lengths
    assert len(blackbird) >= 1
    assert len(sparrow) >= 1
    assert len(flint) >= 1

    blackbird = blackbird[0]
    sparrow = sparrow[0]
    flint = flint[0]

    # must have a UUID
    assert len(blackbird.uuid) == 36
    assert len(sparrow.uuid) == 36
    assert len(flint.uuid) == 36

    # must have a serial number
    assert len(blackbird.sn) == 12
    assert len(sparrow.sn) == 12
    assert len(flint.sn) == 12

@pytest.mark.asyncio
async def test_user(api_fixture):
    user = await async_get_user_id_from_token(api_fixture.api_url, api_fixture.access_token)

    #check we got a UUID
    assert len(user) == 36

@pytest.mark.parametrize("uuid", uuid_list)
@pytest.mark.asyncio
async def test_hp_log(api_fixture, uuid):
    heatpump = HeatPump(api_fixture.api_url, uuid)

    # if the API is changed, this call will fail on a python validation error
    try:
        await heatpump.async_get_status(api_fixture.access_token)
    except ValidationError as e:
        print(f'Validation unsuccessful: {e}')
        pytest.fail('Validation failed')

    except UnauthorizedException as e:
        pytest.fail('get_status call failed')
    except ForbiddenException as e:
        pytest.fail('get_status call failed')
    except Exception as e:
        pytest.fail('get_status call failed')

    # check that all core values are present
    assert heatpump.water_inlet_temperature >= 10
    assert heatpump.water_outlet_temperature >= 10
    assert heatpump.air_inlet_temperature >= -20
    if heatpump.air_outlet_temperature is not None: # flint does not have an air out sensor
        assert heatpump.air_outlet_temperature >= -20
    if heatpump.water_house_in_temperature is not None: # indoor unit may be disconnected
        assert heatpump.water_house_in_temperature >= -1
    if heatpump.thermostat_room_temperature_setpoint is not None: #thermostat may be disconnected
        assert heatpump.thermostat_room_temperature_setpoint >= -1
    if heatpump.thermostat_room_temperature is not None:  #thermostat may be disconnected
        assert heatpump.thermostat_room_temperature >= -1
    assert heatpump.power_input >= 0
    assert heatpump.power_output >= 0
    assert heatpump.compressor_rpm >= 0
    assert heatpump.heat_pump_state in HeatPump.State
    assert heatpump.energy_total >= 0
    assert heatpump.energy_output >= 0






