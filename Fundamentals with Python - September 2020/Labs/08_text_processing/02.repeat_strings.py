def multiply_by_len():
    words = input().split()
    output = ""
    for word in words:
        output += word * len(word)
    print(output)


multiply_by_len()

# words = input().split()
# output = ""
# for word in words:
#     output += word * len(word)
# print(output)
