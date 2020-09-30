from explorer_api import rpc, utils


class TestRPC:
    example_address = (
        "nano_3x4ui45q1cw8hydmfdn4ec5ijfdqi4ryp14g4ayh71jcdkwmddrq7ca9xzn9"
    )
    example_hash = "CD0A56F7729EBBF62A81235AF34D1D69362F1FCD2542734BD8FEBD9D2EB6C130"

    def test_account_history(self, monkeypatch):
        monkeypatch.setattr(utils.Caller, "call", lambda x: x)
        response = rpc.account_history(self.example_address, 5, 2)
        expected_response = {
            "action": "account_history",
            "account": self.example_address,
            "count": 2,
            "offset": 10,
        }
        assert response == expected_response

    def test_account_info(self, monkeypatch):
        monkeypatch.setattr(utils.Caller, "call", lambda x: x)
        response = rpc.account_info(self.example_address, True, False, True)
        expected_response = {
            "action": "account_info",
            "account": self.example_address,
            "representative": True,
            "weight": False,
            "pending": True,
        }
        assert response == expected_response

    def test_block_info(self, monkeypatch):
        monkeypatch.setattr(utils.Caller, "call", lambda x: x)
        response = rpc.block_info(self.example_hash)
        expected_response = {
            "action": "block_info",
            "json_block": True,
            "hash": self.example_hash,
        }
        assert response == expected_response

    def test_delegators(self, monkeypatch):
        monkeypatch.setattr(utils.Caller, "call", lambda x: x)
        response = rpc.delegators(self.example_address)
        expected_response = {
            "action": "delegators",
            "account": self.example_address,
        }
        assert response == expected_response

    def test_pending(self, monkeypatch):
        monkeypatch.setattr(utils.Caller, "call", lambda x: x)
        response = rpc.pending(self.example_address, 5, False)
        expected_response = {
            "action": "pending",
            "account": self.example_address,
            "count": 5,
            "source": False,
        }
        assert response == expected_response
