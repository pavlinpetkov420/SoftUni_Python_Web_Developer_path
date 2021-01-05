nums_str = input().split()

result = list(sorted(nums_str, reverse=True))
print("".join(result))

