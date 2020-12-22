input_count = int(input())
left_sum = 0
right_sum = 0
total_inputs = input_count * 2
for i in range(total_inputs):
    number = int(input())
    if i < input_count:
        left_sum += number
    elif i >= input_count:
        right_sum += number
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(left_sum - right_sum)
    print(f"No, diff = {difference}")
