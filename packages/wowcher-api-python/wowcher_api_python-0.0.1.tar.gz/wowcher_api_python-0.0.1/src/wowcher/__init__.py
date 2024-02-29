import os

from .api import WowcherApi
from .api_mock import WowcherApiMock
from .frame import WowcherPaymentFrame


WowcherApi = WowcherApi if os.environ.get('WOWCHER_API_MOCK', "False") != "True" else WowcherApiMock
