days_in_hotel = int(input())
type_of_room = input()
rating = input()
total_price = 0
discount = 0
if type_of_room == 'room for one person':
    total_price = (days_in_hotel - 1) * 18.0
elif type_of_room == 'apartment':
    total_price = total_price = (days_in_hotel - 1) * 25.0
elif type_of_room == 'president apartment':
    total_price = (days_in_hotel - 1) * 35.0
if days_in_hotel < 10:
    if type_of_room == 'apartment':
        discount = total_price * 0.30
    elif type_of_room == 'president apartment':
        discount = total_price * 0.10
elif 10 <= days_in_hotel <= 15:
    if type_of_room == 'apartment':
        discount = total_price * 0.35
    elif type_of_room == 'president apartment':
        discount = total_price * 0.15
elif days_in_hotel > 15:
    if type_of_room == 'apartment':
        discount = total_price * 0.50
    elif type_of_room == 'president apartment':
        discount = total_price * 0.20
total_price -= discount
if rating == 'positive':
    total_price += total_price * 0.25
elif rating == 'negative':
    total_price *= 0.90
print('{:.2f}'.format(total_price))