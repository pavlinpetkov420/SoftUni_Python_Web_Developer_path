def validate_dates():
    import re
    dates = input()
    pattern = r"(?P<day>\d{2})(\.|-|\/)(?P<month>[A-Z][a-z]{2})(\2)(?P<year>\d{4})"
    matches = re.finditer(pattern, dates)
    for match in matches:
        print(f"Day: {match['day']}, Month: {match['month']}, Year: {match['year']}")


validate_dates()
