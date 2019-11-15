def nb_year(p0, percent, aug, p):
    res = 0
    while(p0 < p):
        res = res + 1
        p0 = int(p0 * (1 + (percent / 100))) + aug
    return res

if __name__=='__main__':
    print(nb_year(1000, 2, 50, 1200))