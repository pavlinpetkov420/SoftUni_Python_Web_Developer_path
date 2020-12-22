tour_price = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())
total_money = puzzles * 2.60 + talking_dolls * 3.00\
              + teddy_bears * 4.10 + minions * 8.20 \
              + trucks * 2.00
toys_count = puzzles + talking_dolls + teddy_bears\
             + minions + trucks
if toys_count >= 50:
    total_money -= (total_money * 0.25)
total_money -= (total_money * 0.10)
money_left_or_needed = abs(total_money - tour_price)
if total_money >= tour_price:
    print(f"Yes! {money_left_or_needed:.2f} lv left.")
else:
    print(f"Not enough money! {money_left_or_needed:.2f} lv needed.")