# You can do it!
nums_str = input().split(", ")
beggars_count = int(input())

numbers = []
for el in nums_str:
    number = int(el)
    numbers.append(number)

beggars = []
for i in range(beggars_count):
    beggars.append(0)
    if len(beggars) == beggars_count:
        break

index = 0

for el in numbers:
    beggars[index] += el
    index += 1
    if index == beggars_count:
        index = 0

print(beggars)
