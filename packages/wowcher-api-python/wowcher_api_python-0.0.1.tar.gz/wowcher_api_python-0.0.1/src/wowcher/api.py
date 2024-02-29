import requests


class WowcherApi:
    ACTIVATION_ROUTE = '/ext/voucher/activate'
    ACTIVATION_LIST_ROUTE = '/ext/voucher/activate/list'

    def __init__(self, api_key, base_url='https://wowcher.app/'):
        self.base_url = base_url
        self.api_url = f"{base_url}/api/v1"
        self.api_key = api_key

    def activate_voucher(self, code) -> dict:
        url = f'{self.api_url}{self.ACTIVATION_ROUTE}'
        headers = {
            "X-ApiKey": self.api_key
        }

        return self.request(url, {"code": code}, headers=headers)

    def activate_vouchers_list(self, codes: list) -> dict:
        url = f'{self.api_url}{self.ACTIVATION_LIST_ROUTE}'
        headers = {
            "X-ApiKey": self.api_key
        }

        return self.request(url, {"codes": codes}, headers=headers)

    def get_frame_url(self, client_id, merchant_id, activation_callback_url):
        url = f'{self.base_url}/en/payment-frame'
        query = f'?client_id={client_id}&merchant_id={merchant_id}&activation_callback_url={activation_callback_url}'

        return f'{url}{query}'

    def request(self, url, json, headers=None):
        result = requests.post(url, json=json, headers=headers)

        # check result data code
        if result.status_code != 200:
            raise Exception("Invalid wowcher provider response")

        return result.json()
