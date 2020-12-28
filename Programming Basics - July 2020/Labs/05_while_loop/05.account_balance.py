command = input()
account_balance, \
    money_input = 0, 0
while command != "NoMoreMoney":
    money_input = float(command)
    if money_input < 0:
        print("Invalid operation!")
        break
    account_balance += money_input
    print(f"Increase: {money_input:.2f}")
    command = input()
print(f"Total: {account_balance:.2f}")
