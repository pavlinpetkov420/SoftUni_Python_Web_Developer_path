quantity_for_type = int(input())
days_left = int(input())
total_cost, \
    day, \
    points = 0, 1, 0
is_third_day = False
while days_left >= day:
    if day % 2 == 0:
        total_cost += (quantity_for_type * 2)
        points += 5
    if day % 3 == 0:
        is_third_day = True
        total_cost += (quantity_for_type * 5) + (quantity_for_type * 3)
        points += 13
    if day % 5 == 0:
        total_cost += (quantity_for_type * 15)
        points += 17
        if is_third_day:
            points += 30
    if day % 10 == 0:
        total_cost += 23
        points -= 20
    if day % 11 == 0:
        quantity_for_type += 2
    if days_left == day and day % 10 == 0:
        points -= 30
    is_third_day = False
    day += 1

print(f"Total cost: {total_cost}\n"
      f"Total spirit: {points}")
