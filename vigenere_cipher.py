keylen = 1
alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g':0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

def decrypt(ciphertext, key):
    plaintext = ''
    for i in range(len(ciphertext)):
        p = list(alphabet.keys()).index(ciphertext[i])
        k = list(alphabet.keys()).index(key)
        c = (p - k) % 26
        plaintext += list(alphabet.keys())[c]
    return plaintext

def crackKey():
    for letter in ciphertext:
        keypos = 0
        if ord(letter) >= 97 and ord(letter) <= 122:
            if ((keypos % keylen) == 0):
                if (alphabet[letter] > 0):
                    alphabet[letter] += 1
                else:
                    alphabet[letter] = 1
            keypos += 1
        
    max = (sorted(alphabet, key=alphabet.get, reverse=True))[0]
    keyord = ((ord(max)-ord('e')) % 26) + 97
    key = chr(keyord)
    return key
   
if __name__ == "__main__":
    ciphertext = 'mxoxybkpslzbzlkpbdrfrabzfcoxoxjbkpxdbj'
    key = crackKey()
    plaintext = decrypt(ciphertext, key)
    print(plaintext)
    

