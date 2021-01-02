import sys
# user input data
nums_str = input().split()
nums_to_remove = int(input())
# nums parser
numbers = [int(x) for x in nums_str]

min_number = sys.maxsize
for i in range(nums_to_remove):
    for el in numbers:
        if el < min_number:
            min_number = el
    numbers.remove(min_number)
    min_number = sys.maxsize

print(numbers)
