input_count = int(input())
# N % 2 == 0
type1_counter = 0
# N % 3 == 0
type2_counter = 0
# N % 4 == 0
type3_counter = 0
for index in range(0, input_count):
    number = int(input())
    if number % 2 == 0:
        type1_counter += 1
    if number % 3 == 0:
        type2_counter += 1
    if number % 4 == 0:
        type3_counter += 1
type1_percentage = type1_counter / input_count * 100
type2_percentage = type2_counter / input_count * 100
type3_percentage = type3_counter / input_count * 100
print(f"{type1_percentage:.2f}%\n{type2_percentage:.2f}%\n{type3_percentage:.2f}%")
