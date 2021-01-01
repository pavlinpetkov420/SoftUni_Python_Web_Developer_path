import math

adv_members = int(input())
adv_days = int(input())

coins = 0
is_mp = False
for day in range(1, adv_days + 1):
    if day % 15 == 0:
        adv_members += 5
    if day % 10 == 0:
        adv_members -= 2
    coins += 50 - (adv_members * 2)
    if day % 3 == 0:
        is_mp = True
        coins -= (adv_members * 3)
    if day % 5 == 0:
        coins += (20 * adv_members)
        if is_mp:
            coins -= adv_members * 2
    is_mp = False

coins_per_member = math.floor(coins / adv_members)
print("{} companions received {} coins each.".format(adv_members, coins_per_member))
