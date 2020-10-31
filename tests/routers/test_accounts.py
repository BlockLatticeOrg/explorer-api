import pytest

from explorer_api.utils import Caller

example_address = "nano_3x4ui45q1cw8hydmfdn4ec5ijfdqi4ryp14g4ayh71jcdkwmddrq7ca9xzn9"
example_hash = "CD0A56F7729EBBF62A81235AF34D1D69362F1FCD2542734BD8FEBD9D2EB6C130"

account_history_expected_response = {
    "account": example_address,
    "history": [],
    "previous": "previous",
}

account_info_expected_response = {
    "account_version": 2,
    "balance": 100000,
    "block_count": 1000,
    "confirmation_height": 999,
    "confirmation_height_frontier": example_hash,
    "frontier": example_hash,
    "modified_timestamp": 10000,
    "open_block": example_hash,
    "pending": 0,
    "representative": example_address,
    "representative_block": example_hash,
    "weight": 100000,
}

delegators_expected_response = {"delegators": {example_address: 10000}}

pending_expected_response = {
    "blocks": {example_hash: {"amount": 1000, "source": example_address}}
}


@pytest.mark.parametrize(
    "endpoint,expected_response",
    [
        ("history", account_history_expected_response),
        ("info", account_info_expected_response),
        ("delegators", delegators_expected_response),
        ("pending", pending_expected_response),
    ],
)
def test_accounts_endpoints(monkeypatch, test_client, endpoint, expected_response):
    monkeypatch.setattr(Caller, "call", lambda _: expected_response)
    response = test_client.get(f"/v1/accounts/{example_address}/{endpoint}")
    assert response.status_code == 200
    assert response.json() == expected_response
