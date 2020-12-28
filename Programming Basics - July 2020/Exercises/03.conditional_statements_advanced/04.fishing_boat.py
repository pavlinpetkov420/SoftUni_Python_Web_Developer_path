budget = float(input())
season = input()
fishers = int(input())
total_price = 0.0
if season == 'Spring':
    total_price += 3000
elif season == 'Summer' or season == 'Autumn':
    total_price += 4200
elif season == 'Winter':
    total_price += 2600
if fishers <= 6:
    total_price *= 0.90
elif 7 <= fishers <= 11:
    total_price *= 0.85
elif fishers >= 12:
    total_price *= 0.75
is_extra_discount_season = season == 'Spring' or season == 'Summer' or season == 'Winter'
if is_extra_discount_season and fishers % 2 == 0:
    total_price *= 0.95
if budget >= total_price:
    money_left = budget - total_price
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_needed = total_price - budget
    print(f'Not enough money! You need {money_needed:.2f} leva.')