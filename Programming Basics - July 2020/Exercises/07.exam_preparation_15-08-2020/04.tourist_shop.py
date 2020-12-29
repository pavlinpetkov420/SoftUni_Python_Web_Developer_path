budget = float(input())

product_counter = 0
money_spend = 0
command = input()
while True:

    if command == "Stop":
        print(f"You bought {product_counter} products for {money_spend:.2f} leva.")
        break

    product_name = command
    product_price = float(input())
    product_counter += 1
    if product_counter % 3 == 0 and product_counter != 0:
        product_price /= 2

    budget -= product_price
    money_spend += product_price
    if budget <= 0:
        money_needed = abs(budget)
        print(f"You don't have enough money!\n"
              f"You need {money_needed:.2f} leva!")
        break

    command = input()
