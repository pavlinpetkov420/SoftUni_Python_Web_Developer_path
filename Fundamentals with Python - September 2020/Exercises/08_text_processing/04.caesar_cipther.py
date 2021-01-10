def encrypt_by_caesar(text):
    encrypted_res = ""
    for symbol in text:
        encrypted_value = ord(symbol) + 3
        encrypted_res += chr(encrypted_value)
    return encrypted_res


decrypted_text = input()
encrypted_text = encrypt_by_caesar(decrypted_text)
print(encrypted_text)
