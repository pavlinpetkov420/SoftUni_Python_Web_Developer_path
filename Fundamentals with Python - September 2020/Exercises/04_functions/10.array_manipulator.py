def exchange_indices(nums_list, i):
    # nums - list of input data, i - index for start the exchange
    if 0 <= i < len(nums_list):
        first_part = nums_list[0:i+1]
        second_part = nums_list[i+1:]
        exchange_list = second_part + first_part
        return exchange_list
    else:
        print("Invalid index")
        return nums_list


def find_max_even(nums_list):

    max_even = -1
    equal_max_index = -1
    is_equal_max_values = False
    for i in range(len(nums_list)):
        if nums_list[i] % 2 == 0:
            if nums_list[i] >= max_even:
                previous_max_even = max_even
                max_even = nums_list[i]
                if previous_max_even == max_even:
                    is_equal_max_values = True
                    equal_max_index = i
                else:
                    is_equal_max_values = False

    if max_even == -1:
        print("No matches")
    elif is_equal_max_values:
        print(equal_max_index)
    else:
        print(nums_list.index(max_even))


def find_max_odd(nums_list):
    max_odd = -1
    previous_max_odd = -1
    equal_max_index = -1
    is_equal_max_values = False
    for i in range(len(nums_list)):
        if nums_list[i] % 2 != 0:
            if nums_list[i] >= previous_max_odd:
                previous_max_odd = max_odd
                max_odd = nums_list[i]
                if previous_max_odd == max_odd:
                    is_equal_max_values = True
                    equal_max_index = i
                else:
                    is_equal_max_values = False

    if max_odd == -1:
        print("No matches")
    elif is_equal_max_values:
        print(equal_max_index)
    else:
        print(nums_list.index(max_odd))


def find_min_even(nums_list):
    # min_even and prev_min_even are with values 1001 because the input constraints of the list are to 1000
    min_even = 1001
    equal_min_index = -1
    is_equal_min_values = False
    for i in range(len(nums_list)):
        if nums_list[i] % 2 == 0:
            if nums_list[i] <= min_even:
                previous_min_even = min_even
                min_even = nums_list[i]
                if previous_min_even == min_even:
                    is_equal_min_values = True
                    equal_min_index = i
                else:
                    is_equal_min_values = False

    if min_even == 1001:
        print("No matches")
    elif is_equal_min_values:
        print(equal_min_index)
    else:
        print(nums_list.index(min_even))


def find_min_odd(nums_list):
    min_odd = 1000
    previous_min_odd = 1000
    equal_min_index = -1
    is_equal_min_values = False
    for i in range(len(nums_list)):
        if nums_list[i] % 2 != 0:
            if nums_list[i] <= previous_min_odd:
                min_odd = nums_list[i]
                previous_min_odd = min_odd
                if previous_min_odd == min_odd:
                    is_equal_min_values = True
                    equal_min_index = i
                else:
                    is_equal_min_values = False

    if min_odd == 1000:
        print("No matches")
    elif is_equal_min_values:
        print(equal_min_index)
    else:
        print(nums_list.index(min_odd))


def print_first_even(nums_list, count):
    # print first X even elements in the data collection
    if count > len(nums_list):
        print("Invalid count")
    else:
        first_even = []
        for el in nums_list:
            if el % 2 == 0:
                first_even.append(el)
                if count == len(first_even):
                    break
        print(first_even)


def print_first_odd(nums_list, count):
    # print first X odd elements in the data collection
    if count > len(nums_list):
        print("Invalid count")
    else:
        first_odd = []
        for el in nums_list:
            if el % 2 != 0:
                first_odd.append(el)
                if count == len(first_odd):
                    break
        print(first_odd)


def print_last_even(nums_list, count):
    if count > len(nums_list):
        print("Invalid count")
    else:
        last_even = []
        for el in nums_list:
            if el % 2 == 0:
                last_even.append(el)
        last_even = last_even[len(last_even) - count:]
        print(last_even)


def print_last_odd(nums_list, count):
    if count > len(nums_list):
        print("Invalid count")
    else:
        last_odd = []
        for el in nums_list:
            if el % 2 != 0:
                last_odd.append(el)
        last_odd = last_odd[len(last_odd) - count:]
        print(last_odd)


input_data = input().split()
numbers = list(map(int, input_data))

while True:
    # split needed action and accompanying data
    # action[0] => main action action[1] => in first 4 cases contains extra info about actions,
    # but in last 2 contains count of needed elements,
    # action[2] => used in 2 last main actions to point extra info about the action
    command = input()
    if command == "end":
        print(numbers)
        break

    action = list(command.split())

    if action[0] == "exchange":
        # split data collection after the given index and exchange the places
        # if the index is invalid, print special message
        index = int(action[1])
        numbers = exchange_indices(numbers, index)

    elif action[0] == "max":
        # find index of max even and odd number in the data collection
        if action[1] == "even":
            find_max_even(numbers)
        elif action[1] == "odd":
            find_max_odd(numbers)

    elif action[0] == "min":
        # find index of min even and odd number in the data collection
        if action[1] == "even":
            find_min_even(numbers)
        elif action[1] == "odd":
            find_min_odd(numbers)

    elif action[0] == "first":

        if action[2] == "even":
            print_first_even(numbers, int(action[1]))
        elif action[2] == "odd":
            print_first_odd(numbers, int(action[1]))

    elif action[0] == "last":
        if action[2] == "even":
            print_last_even(numbers, int(action[1]))
        elif action[2] == "odd":
            print_last_odd(numbers, int(action[1]))
