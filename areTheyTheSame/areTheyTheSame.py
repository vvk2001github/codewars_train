def comp(array1, array2):
    print(array1)
    print(array2)
    if array1 == [] and array2 == []:
        return True

    if len(array1) == 0 or len(array2) == 0:
        return False

    if array1 == None and array2 == None:
        return True
    if array1 == None or array2 == None:
        return False
    if not len(array1) == len(array2):
        return False
    
    tmp = 0
    for i in range(0, len(array1)):
        res = False
        for j in range(0, len(array2)):
            if array1[i]*array1[i] == array2[j]:
                tmp += 1
                array2.remove(array2[j])
                break
    return tmp == len(array1)

if __name__ == '__main__':
    print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 36100, 25921, 361, 20736, 361]))