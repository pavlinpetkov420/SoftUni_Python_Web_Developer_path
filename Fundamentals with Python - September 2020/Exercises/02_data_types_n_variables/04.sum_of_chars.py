input_data = int(input())
add = 0
for i in range(input_data):
    symbol = input()
    add += ord(symbol)
print("The sum equals: {}".format(add))
