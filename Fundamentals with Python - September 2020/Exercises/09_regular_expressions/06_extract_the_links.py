import re


def extract_links():
    pattern = r"(www\.([A-Za-z0-9-]+)(\.[a-z]+){1,})"
    output = ""
    while True:
        cmd = input()
        if cmd == "":
            print(output)
            break
        match = re.finditer(pattern, cmd)
        for el in match:
            output += f"{el.group()}\n"


extract_links()