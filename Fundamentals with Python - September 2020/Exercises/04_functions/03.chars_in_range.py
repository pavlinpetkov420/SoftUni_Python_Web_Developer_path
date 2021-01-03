def find_chars(start, end, chars_as_str=""):
    for symbol in range(start, end + 1):
        chars_as_str += chr(symbol) + " "
    return chars_as_str


first_symbol = ord(input()) + 1
second_symbol = ord(input()) - 1
chars_str = find_chars(first_symbol, second_symbol)
print(chars_str)
