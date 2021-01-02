def find_evens(nums, res):
    for index in range(len(nums)):
        if (nums[index] % 2 == 0) or (nums[index] == 0):
            res.append(nums[index])
    return res


def find_odds(nums, res):
    for index in range(len(nums)):
        if nums[index] % 2 != 0:
            res.append(nums[index])
    return res


def find_negatives(nums, res):
    for index in range(len(nums)):
        if nums[index] < 0:
            res.append(nums[index])
    return res


def find_positives(nums, res):
    for index in range(len(nums)):
        if nums[index] >= 0:
            res.append(nums[index])
    return res


inputs_count = int(input())
numbers_list, \
    result = list(), list()
for inp in range(inputs_count):
    number = int(input())
    numbers_list.append(number)
command = input()
if command == "even":
    result = find_evens(numbers_list, result)
elif command == "odd":
    result = find_odds(numbers_list, result)
elif command == "negative":
    result = find_negatives(numbers_list, result)
else:
    result = find_positives(numbers_list, result)
print(result)
