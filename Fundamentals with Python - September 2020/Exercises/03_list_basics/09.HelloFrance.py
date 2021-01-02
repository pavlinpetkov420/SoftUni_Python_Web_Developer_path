raw_data = input().split("|")
budget = float(input())

new_prices = []
profit = 0

for element in raw_data:
    data = element.split("->")
    name = data[0]
    price = float(data[1])

    clothes_max, \
        shoes_max, \
        accessories_max = 50.00, 35.00, 20.50

    if price <= budget:
        if name == "Clothes":
            if price <= clothes_max:
                budget -= price
                new_price = price * 1.40
                profit += price * 0.40
                new_prices.append(new_price)
        elif name == "Shoes":
            if price <= shoes_max:
                budget -= price
                new_price = price * 1.40
                profit += price * 0.40
                new_prices.append(new_price)
        elif name == "Accessories":
            if price <= accessories_max:
                budget -= price
                new_price = price * 1.40
                profit += price * 0.40
                new_prices.append(new_price)

total_income = budget
for new_price in new_prices:
    total_income += new_price
    print(round(new_price, 2), end=" ")

print()
print(f"Profit: {round(profit, 2)}")
if total_income >= 150.00:
    print("Hello, France!")
else:
    print("Time to go.")
