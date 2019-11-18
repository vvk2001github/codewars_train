def dig_pow(n, p):
    arr = []
    tmp = n
    while tmp >= 1:
        arr.insert(0, tmp % 10)
        tmp = tmp // 10
    tmp = 0
    len_arr = len(arr)
    for i in range(0, len_arr):
        tmp += arr[i] ** (i + p)
    if (tmp % n) == 0:
        return tmp // n
    return -1

if __name__ == '__main__':
    print(dig_pow(46288, 3))