number_border = int(input())
result = 1
previous_number = 0
while result <= number_border:
    print(result)
    previous_number = result
    result = previous_number * 2 + 1
