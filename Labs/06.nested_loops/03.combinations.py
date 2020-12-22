result = int(input())
result_counter = 0
for first_number in range(0, result + 1):
    for second_number in range(0, result + 1):
        for third_number in range(0, result + 1):
            if first_number + second_number + third_number == result:
                result_counter += 1
print(result_counter)