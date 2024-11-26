import pytest

# List all fixtures so that there is no need to import them everywhere
pytest_plugins = [
    "tests.api_fixture",
]

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


