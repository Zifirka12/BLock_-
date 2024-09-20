from sorting import Category, Product


def test_product_creation() -> None:
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_setter_getter() -> None:
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product.price = 200000.0
    assert product.price == 200000.0
    product.price = -100
    assert product.price == 200000.0


def test_category_creation() -> None:
    category = Category("Смартфоны", "Лучшие смартфоны 2023 года", [])
    assert category.name == "Смартфоны"
    assert category.description == "Лучшие смартфоны 2023 года"
    assert len(category.products) == 0


if __name__ == "__main__":
    test_product_creation()
    test_price_setter_getter()
    test_category_creation()
