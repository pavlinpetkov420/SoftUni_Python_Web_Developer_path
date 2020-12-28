money_for_vacation = float(input())
money_on_hand = float(input())
days_counter, \
    spend_days_counter = 0, 0
is_spend_counter_5 = False
while True:
    if spend_days_counter == 5:
        print(f"You can't save the money.\n"
              f"{days_counter}")
        break
    elif money_on_hand >= money_for_vacation:
        print(f"You saved the money for {days_counter} days.")
    command = input()
    money = float(input())
    days_counter += 1
    if command == "save":
        money_on_hand += money
        spend_days_counter = 0
    elif command == "spend":
        money_on_hand -= money
        spend_days_counter += 1
        if money_on_hand < 0:
            money_on_hand = 0
