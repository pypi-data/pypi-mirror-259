class WowcherPaymentFrame:
    def __init__(self, base_url='https://wowcher.app/'):
        self.base_url = base_url

    def get_frame_url(self, client_id, merchant_id, activation_callback_url):
        url = f'{self.base_url}/en/payment-frame'
        query = f'?client_id={client_id}&merchant_id={merchant_id}&activation_callback_url={activation_callback_url}'

        return f'{url}{query}'
