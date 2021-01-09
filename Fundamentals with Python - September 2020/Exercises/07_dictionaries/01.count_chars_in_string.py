text = input()
chars_dictionary = {}

for index in range(len(text)):
    symbol = text[index]
    if symbol != ' ':
        if symbol in chars_dictionary.keys():
            chars_dictionary[symbol] += 1
        else:
            chars_dictionary[symbol] = 1

for key, value in chars_dictionary.items():
    print(f"{key} -> {value}")
