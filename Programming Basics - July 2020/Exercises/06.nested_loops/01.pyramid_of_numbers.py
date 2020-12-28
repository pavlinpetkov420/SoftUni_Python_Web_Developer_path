number = int(input())
counter = 0
is_counter_bigger_than_number = False
for row in range(0, number + 1):
    for column in range(0, row + 1):
        counter += 1
        if counter > number:
            is_counter_bigger_than_number = True
            break
        print(str(counter) + " ", end="")
        if is_counter_bigger_than_number:
            break
    print()
