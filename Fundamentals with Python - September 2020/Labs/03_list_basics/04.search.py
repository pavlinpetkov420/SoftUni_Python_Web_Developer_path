input_count = int(input())
keyword = input()
text_list = list()
filtered_text = list()
for n in range(input_count):
    text = input()
    text_list.append(text)
    if keyword in text:
        filtered_text.append(text)
print("{}\n"
      "{}".format(text_list, filtered_text))
