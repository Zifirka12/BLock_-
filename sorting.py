from typing import Any


class Product:
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
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        return "\n".join([f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
                          for product in self._products])
