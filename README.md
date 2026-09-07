# Inventory Management Basics

A small demo of using a Python dictionary to model an inventory system, including basic operations and a function that makes decisions based on stock levels.

## What's covered
- **Basic operations**: creating an inventory dictionary, accessing quantities by product name, adding new products
- **Iteration**: looping over products and quantities with `.items()`
- **Safe access**: using `.get()` with a default fallback for products that don't exist
- **Selling logic**: checking current stock before allowing a sale, and reducing quantity only if enough stock is available

## How to run
```bash
python inventory_system.py
```

## What I learned
- Using a dictionary to represent real-world inventory (product name → quantity)
- Combining `.get()` with a conditional check to make a decision (can this sale happen or not?)
- Preventing invalid actions (selling more than available stock) instead of letting the data go negative silently
