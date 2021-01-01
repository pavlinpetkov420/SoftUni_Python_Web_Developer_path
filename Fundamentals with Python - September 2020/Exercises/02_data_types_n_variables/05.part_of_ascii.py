start = int(input())
end = int(input())

for index in range(start, end + 1):
    symbol = ""
    symbol = chr(index)
    print(symbol, end=" ")
