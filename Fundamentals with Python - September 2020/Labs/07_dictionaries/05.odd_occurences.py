data = input().split()
occurrences = {}

for datum in data:
    datum = datum.lower()
    if datum in occurrences:
        occurrences[datum] += 1
    else:
        occurrences[datum] = 1

for lang, times in occurrences.items():
    if times % 2 != 0:
        print(lang, end=' ')

# print([f"{' '.join(lang)}" for lang, times in occurrences.items() if times % 2 != 0])