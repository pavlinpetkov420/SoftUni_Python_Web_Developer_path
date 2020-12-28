budget = float(input())
season = input()
destination = ''
camp_or_hotel = ''
spent_money = 0
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        camp_or_hotel = 'Camp'
        spent_money = budget * 0.30
    elif season == 'winter':
        camp_or_hotel = 'Hotel'
        spent_money = budget * 0.70
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        camp_or_hotel = 'Camp'
        spent_money = budget * 0.40
    elif season == 'winter':
        camp_or_hotel = 'Hotel'
        spent_money = budget * 0.80
elif budget >= 1000:
    destination = 'Europe'
    camp_or_hotel = 'Hotel'
    spent_money = budget * 0.90
print(f'Somewhere in {destination}\n{camp_or_hotel} - {round(spent_money, 2):.2f}')
