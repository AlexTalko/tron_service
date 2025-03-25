from sqlalchemy.orm import Session
import pytest

from crud import create_address_request, get_address_requests
from schemas import AddressRequestCreate


def test_create_address_request(test_db):
    address_data = {
        "address": "TXYZ...",
        "bandwidth": 1000,
        "energy": 2000,
        "trx_balance": 10.5
    }
    address_request = AddressRequestCreate(**address_data)
    created = create_address_request(test_db, address_request)

    assert created.address == address_data["address"]
    assert created.bandwidth == address_data["bandwidth"]
    assert created.energy == address_data["energy"]
    assert created.trx_balance == address_data["trx_balance"]
    assert created.id is not None


def test_get_address_requests(test_db):
    # Create some test data
    addresses = [
        {"address": f"TXYZ{i}", "bandwidth": i * 100, "energy": i * 200, "trx_balance": i * 0.5}
        for i in range(1, 6)
    ]

    for addr in addresses:
        create_address_request(test_db, AddressRequestCreate(**addr))

    # Test pagination
    result = get_address_requests(test_db, skip=1, limit=2)
    assert len(result) == 2
    assert result[0].address == "TXYZ5"  # ordered by created_at desc
    assert result[1].address == "TXYZ4"
