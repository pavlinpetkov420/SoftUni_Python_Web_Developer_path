raw_data = input().split()

products = {}
for index in range(0, len(raw_data), 2):
    key = raw_data[index]
    value = raw_data[index + 1]
    products[key] = value

searched = input().split()

for product in searched:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
