# 0.056 time
def reverse_and_save_in_template():
    template = ""
    while True:
        command = input()
        if command == "end":
            return template
        word = command
        reverse_word = word[::-1]
        template += f"{word} = {reverse_word}\n"


output = reverse_and_save_in_template()
print(output)


# 0.087 time
# output  = ""
# while True:
#     command = input()
#     if command == "end":
#         print(output)
#         break
#     word = command
#     reverse_word = word[::-1]
#     output += f"{word} = {reverse_word}\n"
