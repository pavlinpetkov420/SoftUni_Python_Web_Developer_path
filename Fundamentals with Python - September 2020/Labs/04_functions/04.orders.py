def calculate_price(product, quantity):
    cost = 0.0
    if product == "coffee":
        cost = quantity * 1.50
    elif product == "water":
        cost = quantity * 1.00
    elif product == "coke":
        cost = quantity * 1.40
    else:
        cost = quantity * 2.00
    return f"{cost:.2f}"


order_type = input()
amount = int(input())
total_cost = calculate_price(order_type, amount)
print(total_cost)
