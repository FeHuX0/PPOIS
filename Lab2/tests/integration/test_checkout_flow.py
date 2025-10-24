
from src.minimarket.customers.Customer import Customer
from src.minimarket.payments.PaymentProcessor import PaymentProcessor
from src.minimarket.products.Product import Product

def test_checkout_flow():
    cust = Customer('c1','me@example.com','pass123')
    cart = cust.create_cart()
    p = Product('skuX', 20.0, 2)
    cart.add_product(p, qty=1)
    pp = PaymentProcessor('p', [], 0.0)
    order = cart.checkout(cust, pp)
    assert order.customer_id == 'c1'
