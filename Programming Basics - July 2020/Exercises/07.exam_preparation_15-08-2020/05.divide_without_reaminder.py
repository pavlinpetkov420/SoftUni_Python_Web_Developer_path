input_count = int(input())
"""first_type - % 2 == 0
    second_type - % 3 == 0
    third_type - % 4 == 0"""
first_type, \
    second_type, \
    third_type = 0, 0, 0

for index in range(0, input_count):
    number = int(input())

    if number % 2 == 0:
        first_type += 1
    if number % 3 == 0:
        second_type += 1
    if number % 4 == 0:
        third_type += 1

first_type_percentage = first_type / input_count * 100
second_type_percentage = second_type / input_count * 100
third_type_percentage = third_type / input_count * 100

print(f"{first_type_percentage:.2f}%\n"
      f"{second_type_percentage:.2f}%\n"
      f"{third_type_percentage:.2f}%\n")
