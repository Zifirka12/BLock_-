from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def price(self) -> float:
        pass


class MixinLog:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.name}: {self.description}, {self.price}, {self.quantity}"


class Product(MixinLog, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self._price = value

    @classmethod
    def new_product(cls, product_info: dict) -> "Product":
        return cls(product_info["name"], product_info["description"], product_info["price"], product_info["quantity"])

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def add(self, other: Any) -> Any:
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных категорий!")
        return self.price * self.quantity + other.price * other.quantity


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Any]) -> None:
        self.name = name
        self.description = description
        self._products = products or []
        Category.category_count += 1
        Category.product_count += len(self._products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты типа Product или его наследников!")
        self._products.append(product)
        Category.product_count += 1

    def get_products(self) -> list:
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self._products]

    @property
    def products(self) -> list:
        return self.get_products()

    def __str__(self) -> str:
        total_items = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_items} шт."

    def average_price(self) -> float:
        try:
            total_price = sum(product.price for product in self._products)
            count_products = len(self._products)

            if count_products == 0:
                return 0

            return total_price / count_products
        except ZeroDivisionError as e:
            return 0


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: Any,
        model: Any,
        memory: Any,
        color: Any,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: Any,
        germination_period: Any,
        color: Any,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
