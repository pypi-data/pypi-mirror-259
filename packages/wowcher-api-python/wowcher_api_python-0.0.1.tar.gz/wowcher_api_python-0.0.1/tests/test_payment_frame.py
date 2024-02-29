from wowcher import WowcherPaymentFrame


def test_get_frame_url():
    frame = WowcherPaymentFrame()
    assert frame.get_frame_url(1, 2, 'https://example.com') == 'https://wowcher.app//en/payment-frame?client_id=1&merchant_id=2&activation_callback_url=https://example.com'
