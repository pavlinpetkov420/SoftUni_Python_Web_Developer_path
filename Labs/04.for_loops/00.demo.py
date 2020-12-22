# for i in range(1, 13):
#     print(i, end=' ')
# print()
# # стъпка 2 - принтира четните
# for y in range(-10, 10, 2):
#     print(y, end=' ')
# print()
# # принтира числа с обратна стъпка
# for k in range(10, 0, -1):
#     print(k, end=' ')
#
# # дава странен резултат
# # step = 2
# # for step in range(step, 16, step):
# #     step *= 2
# #     print(step)
# работа с текст
# index = 0
# text = "SoftUni"
# fourth_symbol = text[4]
# print(fourth_symbol)
# last_symbol = text[len(text) - 1]
# print(last_symbol)
# принтиране на всеки символ на нов ред
text = "paraplaner"
for index in range(0, len(text)):
    print(text[index])

for symbol in text:
    print(symbol)
# обхождане на текст наобратно
for index in range(len(text) - 1, -1, -1):
    print(text[index])
