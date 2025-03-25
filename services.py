from tronpy import Tron
from tronpy.providers import HTTPProvider
from config import settings


def get_tron_address_info(address: str) -> dict:
    # Для mainnet используйте:
    # client = Tron(network="mainnet")

    # Для shasta testnet:
    client = Tron(network="shasta")

    try:
        account = client.get_account(address)
        balance = client.get_account_balance(address)

        return {
            "address": address,
            "bandwidth": account.get("free_net_limit", 0),
            "energy": account.get("energy_limit", 0),
            "trx_balance": balance
        }
    except Exception as e:
        return {
            "address": address,
            "bandwidth": None,
            "energy": None,
            "trx_balance": None
        }
