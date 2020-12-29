import sys
input_count = int(input())
odd_position_sum = 0
odd_position_min = sys.maxsize
odd_position_max = -sys.maxsize
even_position_sum = 0
even_position_min = sys.maxsize
even_position_max = -sys.maxsize
for index in range(1, input_count + 1):
    number = float(input())
    if index % 2 != 0:
        odd_position_sum += number
        if number > odd_position_max:
            odd_position_max = number
        if number < odd_position_min:
            odd_position_min = number
    else:
        even_position_sum += number
        if number > even_position_max:
            even_position_max = number
        if number < even_position_min:
            even_position_min = number
print(f"OddSum={odd_position_sum:.2f},")
if odd_position_min == sys.maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={odd_position_min:.2f},")
if odd_position_max == -sys.maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={odd_position_max:.2f},")
print(f"EvenSum={even_position_sum:.2f},")
if even_position_min == sys.maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={even_position_min:.2f},")
if even_position_max == -sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={even_position_max:.2f}")
