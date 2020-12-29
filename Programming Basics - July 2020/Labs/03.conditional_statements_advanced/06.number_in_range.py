number = int(input())
valid = -100 <= number <= 100 and number != 0
if valid:
    print('Yes')
else:
    print('No')