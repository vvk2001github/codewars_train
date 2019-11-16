def decrypt(encrypted_text, n):

    pass


def encrypt(text, n):
    if text == None or text == '' or n <= 0:
        return text
    result:str
    for i in range(n):
        result = ''
        for i in range(1, len(text), 2):
            result = result + text[i]
        for i in range(0, len(text), 2):
            result = result + text[i]
        text = result
    return result

print(encrypt('This is a test!', 4))