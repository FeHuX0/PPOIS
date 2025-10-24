
from src.minimarket.customers.Account import Account
from src.minimarket.errors.InsufficientFundsError import InsufficientFundsError
def test_account_deposit_withdraw():
    a = Account('acc1', 100.0, 'u1')
    a.deposit(50.0)
    assert a.balance == 150.0
    a.withdraw(25.0)
    assert a.balance == 125.0
    try:
        a.withdraw(1000.0)
        assert False
    except InsufficientFundsError:
        assert True
