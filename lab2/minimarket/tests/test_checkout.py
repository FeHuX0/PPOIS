import pytest
from datetime import date

from minimarket.checkout.Order import Order
from minimarket.checkout.PaymentSession import PaymentSession
from minimarket.checkout.ShoppingCart import ShoppingCart
from minimarket.core.Product import Product
from minimarket.exceptions.InsufficientStockException import InsufficientStockException
from minimarket.exceptions.PaymentAuthorizationException import PaymentAuthorizationException
from minimarket.exceptions.QuantityLimitException import QuantityLimitException
from minimarket.exceptions.ReturnWindowExpiredException import ReturnWindowExpiredException
from minimarket.inventory.StockItem import StockItem
from minimarket.promotions.Coupon import Coupon
from minimarket.support.ReturnRequest import ReturnRequest


def make_product(sku: str, price: float) -> Product:
    return Product(sku=sku, name=f"Item {sku}", base_price=price, tax_rate=0.0)


def test_cart_accumulates_quantities_for_same_product():
    cart = ShoppingCart()
    product = make_product("A1", 5.0)

    cart.add_item(product, 2)
    cart.add_item(product, 3)

    assert cart.items["A1"].quantity == 5


def test_cart_respects_unique_item_limit():
    cart = ShoppingCart(max_unique_items=1)
    cart.add_item(make_product("A1", 5.0), 1)

    with pytest.raises(QuantityLimitException):
        cart.add_item(make_product("B2", 3.0), 1)


def test_cart_applies_coupon_consistently_for_multiple_calculations():
    cart = ShoppingCart()
    cart.add_item(make_product("A1", 10.0), 2)
    coupon = Coupon(code="SAVE10", discount_percentage=10, expires_on=date.today(), usage_limit=1)

    cart.apply_coupon(coupon)

    assert cart.calculate_total() == pytest.approx(18.0)
    assert cart.calculate_total() == pytest.approx(18.0)


def test_order_allocation_requires_available_stock():
    product = make_product("A1", 5.0)
    stock_item = StockItem(product=product, quantity=5)
    cart = ShoppingCart()
    cart.add_item(product, 1)
    order = Order(order_id="ORD1", cart=cart)

    with pytest.raises(InsufficientStockException):
        order.allocate_stock(stock_item, 6)


def test_payment_session_tracks_status_transitions():
    cart = ShoppingCart()
    cart.add_item(make_product("A1", 10.0), 1)
    order = Order(order_id="ORD2", cart=cart)
    session = PaymentSession(session_id="PAY1", order=order, amount_due=10.0)

    session.authorize_payment(4.0)
    assert session.status == "partial"
    assert session.remaining_balance() == pytest.approx(6.0)

    session.authorize_payment(6.0)
    assert session.status == "captured"
    assert session.remaining_balance() == 0.0


def test_payment_session_rejects_non_positive_amount():
    order = Order(order_id="ORD3", cart=ShoppingCart())
    session = PaymentSession(session_id="PAY2", order=order, amount_due=1.0)

    with pytest.raises(PaymentAuthorizationException):
        session.authorize_payment(0.0)


def test_return_request_fails_after_window():
    cart = ShoppingCart()
    product = make_product("A1", 5.0)
    cart.add_item(product, 1)
    order = Order(order_id="ORD4", cart=cart)
    request = ReturnRequest(
        request_id="RET1",
        order=order,
        product=product,
        reason="Damaged",
        days_since_purchase=20,
    )

    with pytest.raises(ReturnWindowExpiredException):
        request.approve()
