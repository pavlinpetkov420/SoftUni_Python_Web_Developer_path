"""Instructions for each word:
    1. 2nd and LAST letters are switched
    2. 1st letter is replaced by ASCII code"""


def decrypter(text):
    ascii_value = 0
    letter = 0
    for word in text:
        ascii_extract = [x for x in word if '0' <= x <= '9']
        ascii_value += [y for y in ascii_extract]
        letter += lambda x: x, ascii_value
    return text


encrypted_text = input().split()
decrypted_text = decrypter(encrypted_text)
