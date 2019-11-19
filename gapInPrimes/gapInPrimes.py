def gap(g, m, n):
    result = None
    arr = []
    tmp = 0
    for i in range(m, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            arr.append(i)
            tmp += 1
            if (tmp > 1) and ((arr[tmp - 1] - arr[tmp - 2]) == g):
                return [arr[tmp - 2], arr[tmp - 1]]
    return result

print(gap(2,100,110))