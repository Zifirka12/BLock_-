from sorting import Category, Product, Smartphone, LawnGrass
import pytest


@pytest.fixture()
def product() -> Product:
    return Product("ы", "ы", 1768.23, 101)#долматинец


@pytest.fixture()
def smartphone() -> Smartphone:
    return Smartphone("ы", "ы", 12345, 1, 100.1, "я", 69, "черный")


@pytest.fixture()
def lawngrass() -> LawnGrass:
    return LawnGrass("ы", "ы", 1488, 123, "я", "люблю", "себя")


@pytest.fixture()
def category(product: Product) -> Category:
    return Category("ы", "ы", [product])


def test_product(product: Product) -> None:
    assert product.name == "ы"
    assert product.description == "ы"
    assert product.price == 1768.23
    assert product.quantity == 101


def test_smart(smartphone: Smartphone) -> None:
    assert smartphone.name == "ы"
    assert smartphone.description == "ы"
    assert smartphone.price == 12345
    assert smartphone.quantity == 1
    assert smartphone.efficiency == 100.1
    assert smartphone.model == "я"
    assert smartphone.memory == 69
    assert smartphone.color == "черный"


def test_lawngrass(lawngrass: LawnGrass) -> None:
    assert lawngrass.name == "ы"
    assert lawngrass.description == "ы"
    assert lawngrass.price == 1488
    assert lawngrass.quantity == 123
    assert lawngrass.country == "я"
    assert lawngrass.germination_period == "люблю"
    assert lawngrass.color == "себя"
