import pytest
from fastapi import status


def test_get_address_info(client):
    test_address = "TXYZ123"
    response = client.post(
        "/address-info/",
        json={"address": test_address}
    )

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["address"] == test_address
    assert "bandwidth" in data
    assert "energy" in data
    assert "trx_balance" in data


def test_get_address_requests(client):
    # First create some test data
    test_addresses = [f"TXYZ{i}" for i in range(1, 6)]
    for addr in test_addresses:
        client.post("/address-info/", json={"address": addr})

    # Test getting the list
    response = client.get("/address-requests/?skip=1&limit=2")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data["items"]) == 2
    assert data["count"] >= 5
    assert data["limit"] == 2
    assert data["offset"] == 1
