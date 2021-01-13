import re


def calculate_total_n_print(fpq_dict):
    # iterate through the dictionary add output as it is needed to be
    # calculate total price and add it at the end of the string
    total_price = 0
    output = "Bought furniture:\n"
    for name, price in fpq_dict.items():
        output += f"{name}\n"
        total_price += price
    output += f"Total money spend: {total_price:.2f}"
    print(output)


def extract_data(cmd, fpq_dict):
    # if there is a match, store it in dictionary {'name': total_price_of_product}
    pattern = r">>(?P<name>\w+)<<(?P<price>\d+|\d+(.\d+))!(?P<quantity>\d+)"
    matches = re.finditer(pattern, cmd)
    if matches:
        name, total_price = "", 0.0
        for el in matches:
            name = el.group('name')
            total_price = float(el.group('price')) * int(el.group('quantity'))
        if name != '':
            fpq_dict[name] = total_price
    return fpq_dict


def gather_data():
    # fpq - furniture price quantity dict
    fpq_dict = {}

    while True:
        cmd = input()
        if cmd == "Purchase":
            calculate_total_n_print(fpq_dict)
            break
        fpq_dict = extract_data(cmd, fpq_dict)


gather_data()