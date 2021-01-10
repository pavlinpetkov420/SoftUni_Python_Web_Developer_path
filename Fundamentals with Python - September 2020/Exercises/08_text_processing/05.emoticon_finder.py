def find_emoticons(text_list):
    result = []
    for word in text_list:
        if word.startswith(':'):
            if word.endswith('.'):
                word = word.replace('.', '')
            result.append(word)
    return result


text = input().split()

emoticons = find_emoticons(text)

print('\n'.join(emoticons))

# this algorithm needs fix 40 / 100
