username = input()
password = input()
while True:
    user_password_input = input()
    if user_password_input == password:
        print("Welcome " + username + "!")
        break

