inp1 = input()
inp2 = input()

prev_text = inp1
text_1 = list(inp1)
text_2 = list(inp2)
output = ""
for index in range(len(inp1)):
    symbol_1 = text_2[index]
    text_1[index] = text_2[index]
    output = "".join(text_1)
    if output != prev_text:
        print(output)
        prev_text = output
