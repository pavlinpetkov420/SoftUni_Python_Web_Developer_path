# Algorithm for finding palindrome number
def palindrome_or_not(nums):
    for index in range(len(nums)):
        num_copy = nums[index]
        digits = []
        while num_copy != 0:
            n = num_copy % 10
            digits.append(n)
            num_copy = num_copy // 10
        reversed_num = ''
        for element in digits:
            reversed_num += str(element)
        reversed_num = int(reversed_num)
        if nums[index] == reversed_num:
            print(True)
        else:
            print(False)
        reversed_num = ''


nums_str = input().split(', ')
numbers = [int(x) for x in nums_str]
palindrome_or_not(numbers)
