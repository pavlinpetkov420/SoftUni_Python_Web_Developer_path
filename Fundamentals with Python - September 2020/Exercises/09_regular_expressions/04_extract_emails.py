# 50/100
import re


def extract_emails():
    text = input()
    pattern = r"(^|(?<=\s))(([a-zA-Z0-9]+)([\.\-_]?)([A-Za-z0-9]+)(@)([a-zA-Z]+([\.\-_][A-Za-z]+)+))(\b|(?=\s))"
    match = re.finditer(pattern, text)
    result = [el.group() for el in match]
    print(" ".join(result))


extract_emails()