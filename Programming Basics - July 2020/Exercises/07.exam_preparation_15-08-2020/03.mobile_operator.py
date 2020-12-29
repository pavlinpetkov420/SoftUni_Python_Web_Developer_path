contract_duration = input()
sub_type = input()
extra_mobile_data = input()
months_for_paying = int(input())

price_for_month = 0
if contract_duration == "one":
    if sub_type == "Small":
        price_for_month = 9.98
    elif sub_type == "Middle":
        price_for_month = 18.99
    elif sub_type == "Large":
        price_for_month = 25.98
    else:
        price_for_month = 35.99
else:
    if sub_type == "Small":
        price_for_month = 8.58
    elif sub_type == "Middle":
        price_for_month = 17.09
    elif sub_type == "Large":
        price_for_month = 23.59
    else:
        price_for_month = 31.79

if extra_mobile_data == "yes":
    if price_for_month <= 10.00:
        price_for_month += 5.50
    elif 10.00 < price_for_month <= 30.00:
        price_for_month += 4.35
    else:
        price_for_month += 3.85

total_price = months_for_paying * price_for_month

if contract_duration == "two":
    total_price *= 0.9625

print(f"{total_price:.2f} lv.")
