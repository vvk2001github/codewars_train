def first_non_repeating_letter(string):
    if string == None or string == '':
        return ''
    len_str = len(string)
    res = -1
    tmp_str = string.upper()
    for i in range(len_str):
        res = -1
        for j in range(len_str):
            #a = tmp_str[i]
            #b = tmp_str[j]
            #print(a)
            #print(b)
            if tmp_str[i] == tmp_str[j] and (not i == j):
                res = i
                break
        if res == -1:
            return string[i]
    if (res > -1):
        return ''

if __name__ == '__main__':
    print(first_non_repeating_letter('stress'))