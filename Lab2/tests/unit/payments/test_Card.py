
from src.minimarket.payments.Card import Card
from src.minimarket.errors.InvalidCardError import InvalidCardError
def test_card_validate_and_charge():
    c = Card('4242424242424242','12/30','123')
    assert c.validate() is True
    assert c.charge(1.0) is True
    c_bad = Card('bad','01/20','000')
    try:
        c_bad.charge(5.0)
        assert False
    except InvalidCardError:
        assert True
