max_first_multiplier = 11
max_second_multiplier = 11
for first_multiplier in range(1, max_first_multiplier):
    for second_multiplier in range(1, max_second_multiplier):
        result = first_multiplier * second_multiplier
        print(f"{first_multiplier} * {second_multiplier} = {result}")
