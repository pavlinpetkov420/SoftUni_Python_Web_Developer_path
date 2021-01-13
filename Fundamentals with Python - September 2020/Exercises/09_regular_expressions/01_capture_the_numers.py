def capture_all_numbers():
    import re
    pattern = r"\d+"
    while True:
        data = input()
        if not data:
            break
        match = re.findall(pattern, data)
        if match:
            print(*match, end=' ')


capture_all_numbers()
