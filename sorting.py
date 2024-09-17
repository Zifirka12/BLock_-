class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.products: list = []
        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        self.products.append(product)
        Category.product_count += 1
