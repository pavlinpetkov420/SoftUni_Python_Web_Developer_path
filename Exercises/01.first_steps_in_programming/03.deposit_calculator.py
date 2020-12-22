deposit_amount = float(input())
term_in_months = int(input())
annual_interest_rate = float(input())

year_rate = deposit_amount * (annual_interest_rate / 100)
monthly_rate = year_rate / 12
total_money = deposit_amount + term_in_months * monthly_rate

print(total_money)