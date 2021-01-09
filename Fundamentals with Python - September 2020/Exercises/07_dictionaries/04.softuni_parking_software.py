def process_data():
    cars = {}
    input_count = int(input())
    for inp in range(0, input_count, 1):
        tokens = input().split()
        command, username = tokens[0], tokens[1]
        if command == "register":
            plate = tokens[2]
            if username in cars.keys():
                print(f"ERROR: already registered with plate number {cars[username]}")
            else:
                cars[username] = plate
                print(f"{username} registered {plate} successfully")
        else:
            if username not in cars.keys():
                print(f"ERROR: user {username} not found")
            else:
                cars.pop(username)
                print(f"{username} unregistered successfully")
    return cars


def print_registered_cars(cars_in):
    for username, plate in cars_in.items():
        print(f"{username} => {plate}")


registered_cars = process_data()
print_registered_cars(registered_cars)
