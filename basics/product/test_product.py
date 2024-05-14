from pytest import fixture
from product.index import Product

@fixture
def sample_product():
    return Product("Shirt", 100, 20)

class TestProduct():
    def test_init(self, sample_product):
        assert sample_product.name == "Shirt"

    def test_calculate_discount(self, sample_product):
        discount = 10
        discounted_price = sample_product.calculate_discount(discount)
        assert discounted_price == 90