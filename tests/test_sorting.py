import pytest

from sorting import Product,Category


@pytest.fixture
def category():
    return Category("Кирпичи", "завод в Чебоксарах")


@pytest.fixture
def product():
    return Product("Нокия", "Бедрок", 1111.11, 52)


def test_product_init(product):
    assert product.name == "Нокия"
    assert product.description == "Бедрок"
    assert product.price == 1111.11
    assert product.quantity == 52


def test_category_init(category):
    assert category.name == "Кирпичи"
    assert category.description == "завод в Чебоксарах"
    assert len(category.products) == 0

    new_category = Category("посудомойка", "приборы для посудомойки")
    assert Category.category_count == 2


def test_product_count_incr(category, product):
    category.add_product(product)
    assert Category.product_count == 1

    another_product = Product("Ноут", "Игровой ноут", 1765.99, 30)
    category.add_product(another_product)
    assert Category.product_count == 2
