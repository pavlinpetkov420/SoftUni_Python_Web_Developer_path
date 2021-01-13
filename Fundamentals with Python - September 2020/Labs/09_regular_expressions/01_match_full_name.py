def match_full_names():
    import re
    text = input()
    pattern = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"
    matches = re.findall(pattern, text)
    print(" ".join(matches))


match_full_names()
