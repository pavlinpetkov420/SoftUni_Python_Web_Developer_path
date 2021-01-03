def even_odd_sum(num_str, output=""):
    even_sum, \
        odd_sum = 0, 0
    for index in range(len(num_str)):
        number = int(num_str[index])
        if number == 0:
            continue
        elif number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number
    output = f"Odd sum = {odd_sum}, Even sum = {even_sum}"
    return output


num_as_str = input()
output_template = even_odd_sum(num_as_str)
print(output_template)
