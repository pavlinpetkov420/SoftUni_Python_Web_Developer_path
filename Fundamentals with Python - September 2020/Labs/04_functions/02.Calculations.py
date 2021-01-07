def calculate(first_num, second_num, operation):
    if operation == "add":
        result = first_num + second_number
    elif operation == "subtract":
        result = first_num - second_num
    elif operation == "multiply":
        result = first_num * second_num
    else:
        result = first_num / second_num
    return int(result)


calculation_type = input()
first_number = int(input())
second_number = int(input())

result_num = calculate(first_number, second_number, calculation_type)
print(result_num)
