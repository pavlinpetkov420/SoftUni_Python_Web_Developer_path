def group_by_tens(numbers, res):
    index, \
        bound = 0, 10
    while len(numbers) > 0:
        res[index] = [x for x in numbers if x <= bound]
        numbers = list(filter(lambda x: x > bound, numbers))
        bound += 10
        index += 1
        if len(numbers) > 0:
            res.append(0)
    return res


def print_results(numbers):
    group = 10
    for i in numbers:
        print(f"Group of {str(group)}'s: {i}")
        group += 10


nums = [int(x) for x in input().split(', ')]
result = [0]
result = group_by_tens(nums, result)
print_results(result)
