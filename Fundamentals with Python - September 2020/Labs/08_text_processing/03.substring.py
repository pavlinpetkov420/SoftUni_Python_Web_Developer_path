replacer = input()
word = input()

while replacer in word:
    word = word.replace(replacer, "")

print(word)