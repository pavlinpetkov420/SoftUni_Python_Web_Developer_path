raw_data = input().split()
products = {}

for index in range(0, len(raw_data), 2):
    key = raw_data[index]
    value = int(raw_data[index + 1])
    products[key] = value
print(products)
