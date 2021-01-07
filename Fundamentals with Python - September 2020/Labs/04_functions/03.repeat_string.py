def repeater(txt, repeats):
    result = ""
    for repeat in range(0, repeats):
        result += text
    return result


text = input()
repeats_count = int(input())
repeated_text = repeater(text, repeats_count)
print(repeated_text)
