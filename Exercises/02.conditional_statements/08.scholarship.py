import math
month_earnings = float(input())
average_grade = float(input())
min_salary = float(input())
social_scholarship = math.floor(min_salary * 0.35)
excellent_scholarship = math.floor(average_grade * 25.0)
is_social_scholarship = False
is_excellent_scholarship = False
if (4.50 < average_grade) and (min_salary > month_earnings):
    is_social_scholarship = True
if average_grade >= 5.50:
    is_excellent_scholarship = True
if is_social_scholarship and is_excellent_scholarship:
    if social_scholarship > excellent_scholarship:s
        print(f'You get a Social scholarship {social_scholarship} BGN')
    elif excellent_scholarship >= social_scholarship:
        print(f'You get a scholarship for excellent results {excellent_scholarship} BGN')
elif is_social_scholarship:
    print(f'You get a Social scholarship {social_scholarship} BGN')
elif is_excellent_scholarship:
    print(f'You get a scholarship for excellent results {excellent_scholarship} BGN')
else:
    print('You cannot get a scholarship!')
