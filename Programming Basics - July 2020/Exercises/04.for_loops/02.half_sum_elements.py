import sys
input_count = int(input())
max_number = -sys.maxsize
sum = 0
for i in range(0, input_count):
    number = int(input())
    if number > max_number:
        max_number = number
    sum += number
sum -= max_number
if sum == max_number:
    print(f"Yes\nSum = {sum}")
elif sum != max_number:
    print(f"No\nDiff = {abs(max_number - sum)}")
