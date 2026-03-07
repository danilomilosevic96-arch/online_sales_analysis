from cart import Cart # pyright: ignore[reportMissingImports]
import random

cart = Cart()

random_products = random.sample(manager.products, 3) # pyright: ignore[reportUndefinedVariable]

for product in random_products:
    cart.add_to_cart(product)

print("\nSadržaj korpe:")
cart.show_cart()

print("Ukupan iznos za naplatu:", cart.calculate_total(), "RSD")