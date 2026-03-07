from product import Product # pyright: ignore[reportMissingImports]
from product_manager import ProductManager # pyright: ignore[reportMissingImports]

manager = ProductManager()

p1 = Product("Gaming Laptop", 150000, 3)
p2 = Product("Telefon", 80000, 10)
p3 = Product("Miš", 2000, 50)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

