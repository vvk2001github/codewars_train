def determinant(matrix):
    if not isinstance(matrix, list):
        raise
    n = len(matrix)
    for i in range(n):
        if not n == len(matrix[i]) or not isinstance(matrix[i], list):
            raise Exception('Not square matrix')

    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0]* matrix[1][1] - matrix[0][1]*matrix[1][0]
    if n > 2:
        res = 0
        for i in range(n):
            minor_i = minor(matrix, i)
            det_i = determinant(minor_i)
            sign = ((-1)**i)
            res += sign * det_i * matrix[i][0]
        return res

def minor(matrix, row):
    n = len(matrix)
    res = []
    for i in range(n):
        if i == row:
            continue
        else:
            res.append([])
        for j in range(1, n):
            res[len(res) - 1].append(matrix[i][j])
    return res

if __name__ == "__main__":
    m1 = [ [1, 3], [2,5]]
    m2 = [ [2,5,3], [1,-2,-1], [1, 3, 4]]
    m3 = [[1]]

    print(determinant(m2))