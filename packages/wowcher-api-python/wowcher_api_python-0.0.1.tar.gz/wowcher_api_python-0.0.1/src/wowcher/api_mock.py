from .api import WowcherApi


class WowcherApiMock(WowcherApi):
    def activate_voucher(self, code) -> dict:
        return {
            "result": "success",
            "data": {
                "code": code,
                "value": 100
            }
        }

    def activate_vouchers_list(self, codes: list) -> dict:
        return {
            "result": "success",
            "data": {
                "items": [{
                    "code": code,
                    "value": 100
                } for code in ["code1", "code2"]]
            }
        }

    def get_frame_url(self, client_id, merchant_id, activation_callback_url):
        url = f'{self.base_url}/en/payment-frame'
        query = f'?client_id={client_id}&merchant_id={merchant_id}&activation_callback_url={activation_callback_url}'

        return f'{url}{query}'
