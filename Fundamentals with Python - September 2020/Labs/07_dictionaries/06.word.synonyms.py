inputs_count = int(input())

words_synonyms = {}

for num in range(0, inputs_count, 1):
    word = input()
    synonym = input()

    if word in words_synonyms:
        words_synonyms[word].append(synonym)
    else:
        words_synonyms[word] = [synonym]

for key, value in words_synonyms.items():
    print(f"{key} - {', '.join(words_synonyms[key])}")

