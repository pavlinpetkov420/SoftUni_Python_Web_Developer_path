input_count = int(input())
# < 200
type1_counter = 0
# 200 >= N <=399
type2_counter = 0
# 400 >= N <= 599
type3_counter = 0
# 600 >= N <= 799
type4_counter = 0
# >= 800
type5_counter = 0
for index in range(1, input_count + 1):
    number = int(input())
    if number < 200:
        type1_counter += 1
    elif 200 <= number <= 399:
        type2_counter += 1
    elif 400 <= number <= 599:
        type3_counter += 1
    elif 600 <= number <= 799:
        type4_counter += 1
    else:
        type5_counter += 1
type1_percentage = type1_counter / input_count * 100
type2_percentage = type2_counter / input_count * 100
type3_percentage = type3_counter / input_count * 100
type4_percentage = type4_counter / input_count * 100
type5_percentage = type5_counter / input_count * 100
print(f"{type1_percentage:.2f}%\n{type2_percentage:.2f}%"
      f"\n{type3_percentage:.2f}%\n{type4_percentage:.2f}%\n{type5_percentage:.2f}%")
