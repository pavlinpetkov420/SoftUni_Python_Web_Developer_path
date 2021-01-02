factor = int(input())
count = int(input())
multiple_values = []
res = 0
for multiple in range(1, count + 1):
    res = multiple * factor
    multiple_values.append(res)
print(multiple_values)
