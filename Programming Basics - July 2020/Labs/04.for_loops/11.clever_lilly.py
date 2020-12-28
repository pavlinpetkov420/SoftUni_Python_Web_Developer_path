age = int(input())
laundry_price = float(input())
price_per_toy = int(input())

toys_counter = 0
saved_money = 0
money_gift = 10
for year in range(1, age+1):
    if year % 2 != 0:
        toys_counter += 1
    else:
        saved_money += money_gift
        saved_money -= 1
        money_gift += 10

money_from_toys = toys_counter * price_per_toy
total_saved_money = saved_money + money_from_toys
if total_saved_money >= laundry_price:
    money_left = total_saved_money - laundry_price
    print(f"Yes! {money_left:.2f}")
else:
    money_needed = laundry_price - total_saved_money
    print(f"No! {money_needed:.2f}")
