from cart import Cart # pyright: ignore[reportMissingImports]
import random

cart = Cart()

p1 = Product("Gaming Laptop", 150000, 3) # pyright: ignore[reportUndefinedVariable]
p2 = Product("Telefon", 80000, 10) # pyright: ignore[reportUndefinedVariable]
p3 = Product("Miš", 2000, 50) # pyright: ignore[reportUndefinedVariable]

for product in random_products: # pyright: ignore[reportUndefinedVariable]
    cart.add_to_cart(product)

