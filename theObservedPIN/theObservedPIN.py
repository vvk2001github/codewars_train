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
    res = []
    for i in range(len(dct[observed[0]])):
        res.append(dct[observed[0]][i])

    for i in range(1, len(observed)):
        tmp = []
        for j in range(len(dct[observed[i]])):
            for k in range(len(res)):
                tmp.append(res[k] + dct[observed[i]][j])
        res = tmp
    return res

if __name__ == '__main__':
    print(get_pins('11'))