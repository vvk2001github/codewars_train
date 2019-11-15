def get_middle(s):
    str_len = len(s)
    if str_len % 2 == 1:
        return s[str_len // 2]
    else:
        return s[(str_len // 2) - 1:(str_len // 2)+1]

if __name__=="__main__":
    print(get_middle('middle'))