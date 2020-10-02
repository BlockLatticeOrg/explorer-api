from explorer_api.utils import Caller


example_address = "nano_3x4ui45q1cw8hydmfdn4ec5ijfdqi4ryp14g4ayh71jcdkwmddrq7ca9xzn9"
example_hash = "CD0A56F7729EBBF62A81235AF34D1D69362F1FCD2542734BD8FEBD9D2EB6C130"

expected_response = {
    "amount": 10000,
    "balance": 20000,
    "block_account": example_address,
    "confirmed": True,
    "contents": {
        "balance": "1000000",
        "destination": example_address,
        "previous": example_hash,
        "signature": example_hash * 2,
    },
    "height": 1000,
    "local_timestamp": 40000000,
}


def test_blocks_endpoint(monkeypatch, test_client):
    monkeypatch.setattr(Caller, "call", lambda _: expected_response)
    response = test_client.get(f"/blocks/{example_hash}")
    assert response.status_code == 200
    assert response.json() == expected_response
