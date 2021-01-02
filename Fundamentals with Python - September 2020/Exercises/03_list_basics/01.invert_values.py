input_data = input()
nums = [int(x) for x in input_data.split()]
inverted_values = []
for index in range(len(nums)):
    number = nums[index]
    if number > 0:
        number *= -1
    elif number < 0:
        number = abs(number)
    inverted_values.append(number)
print(inverted_values)
