movie_budget = float(input())
extras = int(input())
clothes_price = float(input())

decor_price = movie_budget * 0.10
extras_clothes_price = extras * clothes_price
if extras > 150:
    extras_clothes_price *= 0.90
total_expenses = decor_price + extras_clothes_price
money_left_or_needed = abs(movie_budget - total_expenses)
if movie_budget >= total_expenses:
    print('Action!')
    print(f'Wingard starts filming with {money_left_or_needed:.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {money_left_or_needed:.2f} leva more.')
