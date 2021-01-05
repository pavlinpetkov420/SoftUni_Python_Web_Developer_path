# input , split & cast to int from user input
nums = [int(el) for el in input().split(', ')]
# finding index of even numbers and assign them into list
even_nums = [index for index in range (len(nums)) if nums[index] % 2 == 0]
print(even_nums)


# # v2.0 - harder and non readable way
# nums = list(map(int, input().split(', ')))
# even_nums = list(filter(lambda index: nums[index] % 2 == 0, range(len(nums))))
# print(even_nums)
