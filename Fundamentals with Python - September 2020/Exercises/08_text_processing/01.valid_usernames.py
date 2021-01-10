def symbol_validator(name):
    is_valid = True
    for symbol in name:
        if (symbol.isalpha()) or (symbol == '-') or (symbol == "_") or (symbol.isdigit()):
            continue
        else:
            is_valid = False
            return is_valid
    return is_valid


usernames = input().split(', ')

valid_usernames = []
is_symbols_valid = False
for username in usernames:
    if 3 <= len(username) <= 16:
        is_symbols_valid = symbol_validator(username)
        if is_symbols_valid:
            valid_usernames.append(username)

for valid_name in valid_usernames:
    print(valid_name)
