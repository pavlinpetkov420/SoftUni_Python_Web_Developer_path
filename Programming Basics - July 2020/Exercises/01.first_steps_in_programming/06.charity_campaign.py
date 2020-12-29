campaign_days = int(input())
pastry_chefs = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

cakes_money = cakes * 45
waffles_money = waffles * 5.80
pancakes_money = pancakes * 3.20

raised_money = (cakes_money + waffles_money + pancakes_money)\
               * pastry_chefs * campaign_days
total_money_for_donation = raised_money - (raised_money / 8)

print(total_money_for_donation)
