def find_factorial(num):
    factorial = 1
    for number in range(num, 0, -1):
        factorial *= number
    return factorial


first_number = int(input())
second_number = int(input())
first_f = find_factorial(first_number)
second_f = find_factorial(second_number)
result = first_f / second_f
print(f"{result:.2f}")
