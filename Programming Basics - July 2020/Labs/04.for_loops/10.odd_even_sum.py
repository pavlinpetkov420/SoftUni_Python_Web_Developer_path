input_count = int(input())
even_positions_sum = 0
odd_position_sum = 0
for i in range(input_count):
    number = int(input())
    if i % 2 == 0:
        even_positions_sum += number
    else:
        odd_position_sum += number
if even_positions_sum == odd_position_sum:
    print(f"Yes\nSum = {even_positions_sum}")
else:
    difference = abs(even_positions_sum - odd_position_sum)
    print(f"No\nDiff = {difference}")
