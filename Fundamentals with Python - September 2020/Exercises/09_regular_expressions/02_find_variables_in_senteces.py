def validate_variable_names():
    import re

    pattern = r"((?<=^_)|(?<=\s_))(?P<variable>[A-Za-z-0-9]+\b)"
    text = input()
    matches = [el.group("variable") for el in re.finditer(pattern, text)]
    print(",".join(matches))


validate_variable_names()
