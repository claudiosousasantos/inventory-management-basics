# Basic dictionary creation, access, and updates.
def demo_basic_dict_operations():
    inventory = {"Apple": 50, "Banana": 30}
    print(inventory["Apple"])          # Access by key -> 50
    inventory["Orange"] = 20           # Add a new key-value pair
    print(inventory["Orange"])

# Different ways to iterate over a dictionary.
def demo_dict_iteration():
    inventory = {"Apple": 50, "Banana": 30, "Orange": 20}
    # Iterating over keys only
    print("\nIterating over keys:")
    for product in inventory:
        print(product, inventory[product])
    # Iterating over key-value pairs (preferred, more readable)
    print("\nIterating over items:")
    for product, quantity in inventory.items():
        print(product, "has", quantity, "units in stock")

# How to safely check/access a value with a default fallback before selling
def demo_safe_get():
    inventory = {"Apple": 50, "Banana": 30, "Orange": 20}
    # .get() avoids a KeyError if the product doesn't exist
    print("\nSafe get:")
    print(inventory.get("Apple", 0))     # existing key -> 50
    print(inventory.get("Mango", 0))     # missing key -> 0 (no crash)

# Selling an item safely: check stock before reducing quantity
def demo_sell_item(product, amount):
    inventory = {"Apple": 50, "Banana": 30, "Orange": 20}
    current_stock = inventory.get(product, 0)
    if current_stock >= amount:
        inventory[product] = current_stock - amount
        print(f"\nSold {amount} {product}(s). Remaining stock: {inventory[product]}")
    else:
        print(f"\nCannot sell {amount} {product}(s). Only {current_stock} in stock.")

demo_basic_dict_operations()
demo_dict_iteration()
demo_safe_get()
demo_sell_item("Apple", 10)
demo_sell_item("Mango", 5)