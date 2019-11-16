def decrypt(encrypted_text, n):
    if encrypted_text == None or encrypted_text == '' or n <= 0:
        return encrypted_text
    str_len:int = len(encrypted_text)
    half_str_len = str_len // 2
    result: str = ''.ljust(str_len)
    for j in range(n):
        res_list = list(result)
        for i in range(half_str_len):
            res_list[i*2 + 1] = encrypted_text[i]
        for i in range(str_len - str_len // 2):
            res_list[i*2] = encrypted_text[half_str_len + i]
        result = ''.join(res_list)
        encrypted_text = result
    return result


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

print(encrypt('This is a test!', 2))
print(decrypt(' Tah itse sits!', 3))