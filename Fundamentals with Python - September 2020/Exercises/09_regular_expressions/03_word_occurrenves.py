import re

text = input().lower()
word = input()

pattern = fr"(?P<word>{word})(?=$\s|\W)"
matches = [1 for _ in re.findall(pattern, text)]
print(len(matches))
