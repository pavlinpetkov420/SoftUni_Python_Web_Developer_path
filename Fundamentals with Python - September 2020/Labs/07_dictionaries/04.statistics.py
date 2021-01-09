products = {}

while True:
    command = input().split(": ")
    if command[0] == "statistics":
        break
    name, quantity = command[0], int(command[1])

    if name in products:
        products[name] += quantity
    else:
        products[name] = quantity

print('Products in stock:')
# [print(f"- {product}: {quantity}") for product,quantity in products.items()]
for name, value in products.items():
    print(f"- {name}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
