def likes(names):
    if not isinstance(names, list):
        return 'no one likes this'
    if names == []:
        return 'no one likes this'
    list_len = len(names)
    if list_len == 1:
        return names[0] + " likes this"
    if list_len == 2:
        return names[0] + " and " + names[1] + " likes this"
    if list_len == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    if list_len > 3:
        return names[0] + ", " + names[1] + " and " + str(list_len - 2) + " others like this"

if __name__ == '__main__':
    print(likes([]))