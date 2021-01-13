def match_numbers():
    import re

    numbers_str = input()
    pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
    matches = re.finditer(pattern, numbers_str)
    for match in matches:
        print(match.group(0), end=' ')


match_numbers()
