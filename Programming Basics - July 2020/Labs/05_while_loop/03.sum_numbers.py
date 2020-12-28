sum_border = int(input())
result = 0
while True:
    number = int(input())
    result += number
    if result >= sum_border:
        print(result)
        break
