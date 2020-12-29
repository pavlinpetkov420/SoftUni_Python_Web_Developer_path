screening_type = input()
rows = int(input())
columns = int(input())
total_seats = rows * columns
total_income = 0
if screening_type == 'Premiere':
    total_income = total_seats * 12.00
elif screening_type == 'Normal':
    total_income = total_seats * 7.50
elif screening_type == 'Discount':
    total_income = total_seats * 5.00
print('{:.2f} leva'.format(total_income))
