text = input()
text = text.lower()
result = 0
for index in range(0, len(text)):
    symbol = text[index]
    if symbol == 'a':
        result += 1
    elif symbol == 'e':
        result += 2
    elif symbol == 'i':
        result += 3
    elif symbol == 'o':
        result += 4
    elif symbol == 'u':
        result += 5
print(result)
