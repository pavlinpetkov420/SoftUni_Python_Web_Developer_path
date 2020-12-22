start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

iteration_counter = 0
is_combination_valid = False
number_one, \
    number_two = 0, 0

for first_number in range(start_interval, end_interval + 1):
    if is_combination_valid:
        break
    for second_number in range(start_interval, end_interval + 1):
        iteration_counter += 1
        if first_number + second_number == magic_number:
            is_combination_valid = True
            number_one = first_number
            number_two = second_number
            break
if is_combination_valid:
    print(f"Combination N:{iteration_counter} "
          f"({number_one} + {number_two} = {magic_number})")
else:
    print(f"{iteration_counter} combinations - neither equals {magic_number}")
