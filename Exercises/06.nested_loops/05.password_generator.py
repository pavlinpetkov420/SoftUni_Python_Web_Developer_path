first_number = int(input())
second_number = int(input())
first_pass_symbol, \
    second_pass_symbol, \
    third_pass_symbol, \
    fourth_pass_symbol, \
    fifth_pass_symbol = 0, 0, "", "", 0
letter_end_border = chr(97 + second_number)
for first_symbol in range(1, first_number):
    first_pass_symbol = first_symbol
    for second_symbol in range(1, first_number + 1):
        second_pass_symbol = second_symbol
        for third_symbol in range(ord('a'), ord(letter_end_border)):
            third_pass_symbol = chr(third_symbol)
            for fourth_symbol in range(ord('a'), ord(letter_end_border)):
                fourth_pass_symbol = chr(fourth_symbol)
                for fifth_symbol in range(1, first_number + 1):

                    if fifth_symbol > first_pass_symbol and fifth_symbol > second_pass_symbol:
                        fifth_pass_symbol = fifth_symbol
                        print(f"{first_pass_symbol}{second_pass_symbol}{third_pass_symbol}"
                              f"{fourth_pass_symbol}{fifth_pass_symbol} ", end="")
                        continue
