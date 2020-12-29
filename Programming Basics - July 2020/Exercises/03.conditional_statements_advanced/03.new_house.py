# Roses Dahlias Tulips Narcissus Gladiolus
flower_type = input()
flower_amount = int(input())
budget = float(input())
total_price = 0
if flower_type == 'Roses':
    total_price = flower_amount * 5.0
    if flower_amount > 80:
        total_price *= 0.90
elif flower_type == 'Dahlias':
    total_price = flower_amount * 3.80
    if flower_amount > 90:
        total_price *= 0.85
elif flower_type == 'Tulips':
    total_price = flower_amount * 2.80
    if flower_amount > 80:
        total_price *= 0.85
elif flower_type == 'Narcissus':
    total_price = flower_amount * 3.0
    if flower_amount < 120:
        total_price *= 1.15
elif flower_type == 'Gladiolus':
    total_price = flower_amount * 2.50
    if flower_amount < 80:
        total_price *= 1.20
if budget >= total_price:
    money_left = budget - total_price
    print(f'Hey, you have a great garden with {flower_amount} {flower_type} and {money_left:.2f} leva left.')
elif budget < total_price:
    money_needed = total_price - budget
    print(f'Not enough money, you need {money_needed:.2f} leva more.')