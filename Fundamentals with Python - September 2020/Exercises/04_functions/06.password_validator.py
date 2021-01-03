# If some of the validations are not covered print special message for every requirement
def length_validation(secret_code):
    # Valid is when is between 6 and 10 symbols.
    if 6 <= len(secret_code) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def letters_digits_validation(secret_code):
    # ld => stands for only letters and digits in password. Special symbols are forbidden(condition)
    for index in range(len(secret_code)):
        symbol = ord(secret_code[index])
        if (48 <= symbol <= 57) or (65 <= symbol <= 90) or (97 <= symbol <= 122):
            continue
        else:
            print("Password must consist only of letters and digits")
            return False
    return True


def least_two_digits(secret_code):
    # Valid is when have at least 2 digits
    digits_counter = 0
    for index in range(len(secret_code)):
        symbol = ord(secret_code[index])
        if 48 <= symbol <= 57:
            digits_counter += 1
    if digits_counter >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


password = input()
is_len_valid = length_validation(password)
is_only_dl = letters_digits_validation(password)
are_two_digits = least_two_digits(password)

if is_len_valid and is_only_dl and are_two_digits:
    print("Password is valid")
