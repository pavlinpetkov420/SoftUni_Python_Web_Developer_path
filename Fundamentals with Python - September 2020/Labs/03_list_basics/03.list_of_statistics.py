inputs = int(input())
# Stores in list positive numbers(including 0) and in other negative numbers
positive_nums = list()
negative_nums = list()

for i in range(inputs):
    number = int(input())
    if number >= 0:
        positive_nums.append(number)
    else:
        negative_nums.append(number)
output = f"{positive_nums}\n" \
         f"{negative_nums}\n" \
         f"Count of positive: {len(positive_nums)}. Sum of negative: {sum(negative_nums)}"
print(output)
