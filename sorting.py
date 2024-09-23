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

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
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
        self._products.append(product)
        Category.product_count += 1

    def get_products(self) -> list:
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self._products]

    @property
    def products(self) -> list:
        return self.get_products()

    def __str__(self):
        total_items = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_items} шт."


class ProductList:
    def __init__(self, *args):
        self.products = args

    def add_product(self, name, price):
        self.products = (*self.products, (name, price))

    def get_total_cost(self):
        return sum(price * quantity for _, price, quantity in self.products)

    def display_summary(self):
        items = [(name, price) for name, price, _ in self.products]
        return ", ".join(f"{name}: {price}" for name, price in items)

    def __add__(self, other):
        combined_list = ProductList(*self.products, *other.products)
        return combined_list

    def __repr__(self):
        return f"Products({self.display_summary()})"

    def __len__(self):
        return len(self.products)

    def __iter__(self):
        return iter(self.products)
