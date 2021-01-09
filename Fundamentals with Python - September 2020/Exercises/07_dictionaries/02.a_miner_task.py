def print_available_resources(resources):
    for key, value in resources.items():
        print(f"{key} -> {value}")


def process_data():
    resources = {}

    while True:
        command = input()
        if command == "stop":
            return resources
        item = command
        quantity = int(input())

        if item in resources.keys():
            resources[item] += quantity
        else:
            resources[item] = quantity


resource_quantities = process_data()
print_available_resources(resource_quantities)
