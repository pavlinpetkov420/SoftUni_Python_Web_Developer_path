days = int(input())
hours_per_day = int(input())

total_price, \
    day_price = 0, 0

for day in range(1, days + 1):
    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            day_price += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            day_price += 1.25
        else:
            day_price += 1
    print(f"Day: {day} - {day_price:.2f} leva")
    total_price += day_price
    day_price = 0

print(f"Total: {total_price:.2f} leva")

