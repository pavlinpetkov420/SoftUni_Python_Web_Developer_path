def calculate_results(iteration_text, other_text):
    res = 0
    for index in range(len(iteration_text)):
        if index > len(other_text) - 1:
            res += ord(iteration_text[index])
        else:
            res += ord(iteration_text[index]) * ord(other_text[index])
    return res


text_one, text_two = input().split()
result = 0
string_to_iterate = None
if len(text_one) > len(text_two):
    string_to_iterate = text_one
    result = calculate_results(string_to_iterate, text_two)
elif len(text_two) > len(text_one):
    string_to_iterate = text_two
    result = calculate_results(string_to_iterate, text_one)
else:
    result = calculate_results(text_one, text_two)
print(result)
