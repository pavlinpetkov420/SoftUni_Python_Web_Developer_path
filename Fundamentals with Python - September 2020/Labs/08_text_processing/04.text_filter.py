def replace_banned_words(filters, text_to_process):

    for word in filters:
        while word in text_to_process:
            text_to_process = text_to_process.replace(word, '*'*len(word))
    return text_to_process


# user input
banned_words = input().split(', ')
text = input()
# function which replaced all banned words with asterisks
new_text = replace_banned_words(banned_words, text)
print(new_text)
