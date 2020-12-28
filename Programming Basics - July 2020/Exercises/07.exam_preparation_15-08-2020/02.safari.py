budget = float(input())
fuel_needed = float(input())
day_of_weekend = input()
# 100lv. for guide
total_cost = (fuel_needed * 2.10) + 100
# calculating discounts
if day_of_weekend == "Saturday":
    total_cost *= 0.90
else:
    total_cost *= 0.80
# check are money enough or not
if budget >= total_cost:
    money_left = budget - total_cost
    print(f"Safari time! Money left: {money_left:.2f} lv.")
else:
    money_needed = total_cost - budget
    print(f"Not enough money! Money needed: {money_needed:.2f} lv.")