def process_data():
    name_price, \
        name_quantity = {}, {}

    while True:
        command = input()
        if command == "buy":
            return name_price, name_quantity
        tokens = command.split()
        name, price, quantity = tokens[0], float(tokens[1]), int(tokens[2])
        if name in name_price.keys():
            if name_price[name] != price:
                name_price[name] = price
                name_quantity[name] += quantity
        else:
            name_price[name] = price
            name_quantity[name] = quantity


def print_profit(prices, quantities):
    for name, price in prices.items():
        total_price = prices[name] * quantities[name]
        print(f"{name} -> {total_price:.2f}")


price_dict, quantity_dict = process_data()
print_profit(price_dict, quantity_dict)
