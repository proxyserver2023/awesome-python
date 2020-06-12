import pytest
from .wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    '''Returns a wallet instance with zero balance'''
    return Wallet()


@pytest.fixture
def wallet():
    '''Returns a wallet instance with balance == 20'''
    return Wallet(20)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_initial_amount(wallet):
    assert wallet.balance == 20


def test_add_cash(wallet):
    wallet.add_cash(10)
    assert wallet.balance == 30


def test_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10
    

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(wallet):
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)


@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 5, 15),
    (100, 1, 99),
    (0, 0, 0),
])
def test_transactions(empty_wallet, earned, spent, expected):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected
