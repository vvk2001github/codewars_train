def last_digit(n1, n2):
    print('N1 = ', n1)
    print('N2 = ', n2)
    if n2 == 0:
        return 1
    a = n1 % 10
    if n2 == 1:
        return a
    if a == 1 or a == 5 or a == 6:
        return a

    #
    if a == 4 or a == 9:
        b = n2 % 2
        if a == 4:
            if b == 1:
                return 4
            return 6
        if a == 9:
            if b == 1:
                return 9
            return 1

    #
    b = (n2 % 4) - 1
    res2 = [2, 4, 8, 6]
    res3 = [3, 9, 7, 1]
    res7 = [7, 9, 3, 1]
    res8 = [8, 4, 2, 6]

    if a == 2:
        return res2[b]
    if a == 3:
        return res3[b]
    if a == 7:
        return res7[b]
    if a == 8:
        return res8[b]

    return 0

if __name__ == '__main__':
    print(last_digit(9, 7))