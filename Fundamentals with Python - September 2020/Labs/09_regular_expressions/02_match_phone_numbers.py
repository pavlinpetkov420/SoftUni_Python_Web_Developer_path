# \+359([ |-])2\1\d{3}\1\d{4}\b
# \+359( |-)2\1[0-9]{3}\1[0-9]{4}\b

def validate_phone_numbers():
    import re
    phone_numbers = input()
    pattern = r"(\+359( |-)2\2[0-9]{3}\2[0-9]{4}\b)"
    matches = re.findall(pattern, phone_numbers)
    result = [phone for phone, sep in matches]
    print(", ".join(matches))


validate_phone_numbers()
