def add(first, second):
    return first + second


def subtract(first_res, third):
    return first_res - third_num


def add_and_subtract(first, second, third):
    final_result = subtract(add(first, second), third)
    return final_result


first_num = int(input())
second_num = int(input())
third_num = int(input())

result = add_and_subtract(first_num, second_num, third_num)
print(result)
