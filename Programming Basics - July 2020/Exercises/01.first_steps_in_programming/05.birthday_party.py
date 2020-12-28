hall_price = int(input())

cake_price = hall_price * 0.20
drinks_price = cake_price * 0.55
clown_price = hall_price / 3

spent_money = hall_price + cake_price \
              + drinks_price + clown_price

print(spent_money)

