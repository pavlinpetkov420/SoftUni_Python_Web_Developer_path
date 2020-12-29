first_number = int(input())
second_number = int(input())
operator = input()
result = 0
even_or_odd = ''
is_first_three_operators = operator == '+' or operator == '-' or operator == '*'
is_segmentation = operator == '/' or operator == '%'
if is_first_three_operators:
    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    if result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    print(f'{first_number} {operator} {second_number} = {result} - {even_or_odd}')
elif is_segmentation:
    if second_number == 0:
        print(f'Cannot divide {first_number} by zero')
    elif operator == '/':
        result = first_number / second_number
        print(f'{first_number} / {second_number} = {result:.2f}')
    elif operator == '%':
        result = first_number % second_number
        print(f'{first_number} % {second_number} = {result}')
