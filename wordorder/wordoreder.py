def order(sentence):
    tmp = sentence.split()
    dct = {}
    for i in tmp:
        for j in range(len(i)):
            if i[j].isdigit():
                dct[int(i[j])] = i
                break
    dct = sorted(dct.items())
    res = ''
    for i in dct:
        res = res + i[1] + ' '
    return res[:-1]

if __name__ == "__main__":
    print(order('is2 Thi1s T4est 3a'))