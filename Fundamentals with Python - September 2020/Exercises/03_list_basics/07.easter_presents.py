# gifts separated by space
gifts = input().split()

while True:
    tokens = input()

    if tokens == "No Money":
        break
    # separate given command and process tha data
    tokens = tokens.split()
    command = tokens[0]
    new_gift = tokens[1]
    index = None

    if len(tokens) == 3:
        index = int(tokens[2])

    if command == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == new_gift:
                gifts[i] = "None"
    elif command == "Required":
        if 0 <= index < len(gifts):
            gifts[index] = new_gift
    elif command == "JustInCase":
        gifts[len(gifts) - 1] = new_gift

# print every output except "None"
for el in gifts:
    if el == "None":
        continue
    print(f"{el}", end=" ")
