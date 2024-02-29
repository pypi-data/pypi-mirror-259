from wowcher import WowcherApi


def test_activate_voucher():
    api = WowcherApi("api_key")
    result = api.activate_voucher("code")

    assert result == {
        "result": "success",
        "data": {
            "code": "code",
            "value": 100
        }
    }


def test_activate_vouchers_list():
    api = WowcherApi("api_key")
    result = api.activate_vouchers_list(["code1", "code2"])

    data = {
        "items": [
            {
                "code": code,
                "value": 100
            } for code in ["code1", "code2"]
        ]
    }

    assert result == {
        "result": "success",
        "data": data
    }
