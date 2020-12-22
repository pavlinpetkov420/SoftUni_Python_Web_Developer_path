command = input()
while command != "End":
    destination = command
    money_needed = float(input())
    saved_money = 0
    while saved_money < money_needed:
        amount_to_save = float(input())
        saved_money += amount_to_save
    print(f"Going to {destination}!")
    command = input()
