def get_pins(observed):
    dct = {
    '1': ['1', '2', '4'],
    '2': ['2', '1', '3', '5'],
    '3': ['3', '2', '6'],
    '4': ['4', '1', '5', '7'],
    '5': ['5', '2', '4', '6', '8'],
    '6': ['6', '3', '5', '9'],
    '7': ['7', '4', '8'],
    '8': ['8', '7', '5', '9', '0'],
    '9': ['9', '6', '8'],
    '0': ['0', '8'],
    }
    tmp = 1
    for i in range(len(observed)):
        tmp *= len(dct[observed[i]])
    res = [''] * tmp
    for i in range(tmp):
        tmp1 = ''
        for j in range(len(observed)):
            tmp1 = tmp1 + dct[observed[j]][i % len(dct[observed[j]])]
        res[i] = tmp1
    return res

if __name__ == '__main__':
    print(get_pins('11'))