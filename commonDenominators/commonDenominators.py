def convertFracts(lst):

    if lst == None or lst ==[] or lst == [[]]:
        return []
    if len(lst) == 1:
        return lst[0]


    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    def lcm(a, b):
        return a // gcd(a, b) * b

    lcm_res = lcm(lst[0][1], lst[1][1])
    
    for i in range(2, len(lst)):
        lcm_res = lcm(lcm_res, lst[i][1])
    
    for i in range(len(lst)):
        tmp = lcm_res // lst[i][1]
        lst[i][0] *= tmp
        lst[i][1] = lcm_res

    return lst

if __name__=="__main__":
    print(convertFracts([[1, 2], [1, 3], [1, 4]]))