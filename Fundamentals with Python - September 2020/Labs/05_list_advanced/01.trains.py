wagons = int(input())
train = [0 for _ in range(wagons)]

while True:
    command = input()
    if command == "End":
        print(train)
        break
    tokens = command.split()
    action = tokens[0]

    if action == "add":
        people = int(tokens[1])
        train[-1] += people
    elif action == "insert":
        index = int(tokens[1])
        people = int(tokens[2])
        train[index] += people
    elif action == "leave":
        index = int(tokens[1])
        people = int(tokens[2])
        train[index] -= people
