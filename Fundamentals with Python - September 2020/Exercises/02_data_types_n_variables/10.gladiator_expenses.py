lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

is_sword_broken, \
    is_helmet_broken = False, False
shield_counter = 0
total_cost = 0.00

for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        is_helmet_broken = True
        total_cost += helmet_price
    if fight % 3 == 0:
        is_sword_broken = True
        total_cost += sword_price
    if is_sword_broken and is_helmet_broken:
        total_cost += shield_price
        shield_counter += 1
        if shield_counter % 2 == 0:
            total_cost += armor_price
    is_sword_broken = False
    is_helmet_broken = False

print("Gladiator expenses: {:.2f} aureus".format(total_cost))
