def alphabet_position(text):
    return ' '.join(str(ord(x) - 64) for x in text.upper() if x.isalpha())

if __name__=='__main__':
    print(alphabet_position("The sunset sets at twelve o' clock."))