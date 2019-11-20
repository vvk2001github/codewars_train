class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.table = {}
        for i, sym in enumerate(self.alphabet):
            self.table[sym] = alphabet[i:] + alphabet[:i]
        self.len_key = len(self.key)
        #print(self.table)
    
    def encode(self, text):
        res = ''
        for i, sym in enumerate(text):
            if sym in self.alphabet:
                cipher_string = self.table[self.key[i % self.len_key]]
                cipher_sym_pos = self.alphabet.index(sym)
                res = res + cipher_string[cipher_sym_pos]
                #print(self.alphabet.index(sym))
                #res = res + dct[password[i]]
            else:
                res = res + sym
        return res
    
    def decode(self, text):
        res = ''
        for i, sym in enumerate(text):
            if sym in self.alphabet:
                cipher_string = self.table[self.key[i % self.len_key]]
                cipher_sym_pos = cipher_string.index(sym)
                res = res + self.alphabet[cipher_sym_pos]
            else:
                res = res + sym
        return res

if __name__ == "__main__":
    abc = "abcdefghijklmnopqrstuvwxyz"
    key = "password"
    c = VigenereCipher(key, abc)
    print(c.encode('codewars'))
    print(c.decode('rovwsoiv'))

    print()
    print(c.encode('waffles'))
    print(c.decode('laxxhsj'))

    print()
    print(c.encode('CODEWARS'))
    print(c.decode('CODEWARS'))