def split_types_of_chars(text_to_split):
    nums, \
        chars, \
        others = "", "", ""
    for symbol in text_to_split:
        represented = ord(symbol)
        if (65 <= represented <= 90) or (97 <= represented <= 122):
            chars += symbol
        elif 48 <= represented <= 57:
            nums += symbol
        else:
            others += symbol
    return nums, chars, others


def split_types_of_chars_v2(text_to_split):
    nums, \
        chars, \
        others = "", "", ""
    for symbol in text_to_split:
        if symbol.isalpha():
            chars += symbol
        elif symbol.isdigit():
            nums += symbol
        else:
            others += symbol
    return nums, chars, others


text = input()
digits, letters, other = split_types_of_chars_v2(text)
# digits, letters, other = split_types_of_chars(text)
print(f"{digits}\n"
      f"{letters}\n"
      f"{other}")
