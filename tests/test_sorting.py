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


def test_add_product_to_category() -> None:
    category = Category("Смартфоны", "Лучшие смартфоны 2023 года", [])
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0] == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


if __name__ == "__main__":
    test_product_creation()
    test_price_setter_getter()
    test_category_creation()
    test_add_product_to_category()
