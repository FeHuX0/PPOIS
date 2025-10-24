
from src.minimarket.products.Product import Product
def test_product_stock_and_price():
    p = Product('sku1', 10.0, 2)
    assert p.is_available() is True
    p.adjust_stock(-2)
    assert p.is_available() is False
