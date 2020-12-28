divisor = int(input())
bound = int(input())
last_n, \
    max_n = 0, 0
for n in range(1, bound + 1):
    if n % divisor == 0:
        max_n = n
        if last_n > max_n:
            max_n = last_n
        else:
            last_n = max_n
print(max_n)
