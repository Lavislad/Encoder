n = 7
m = 435
CLOSED_KEY = [1, 3, 5, 12, 25, 52, 115, 220]

def CreateOpenKey(closed_key, n, m):
    open_key = []
    for el in closed_key:
        open_key.append(el*n%m)
    return open_key

def FindN1(n, m):
    n1 = 1
    success = False
    while success is False:
        if (n*n1)%m == 1:
            success = True
        else:
            n1+=1
    return n1

def EncodeWord(word):
    bytes_data = word.encode('cp1251')
    binary_str = ' '.join(format(byte, '08b') for byte in bytes_data)
    return binary_str

def DecodeWord(bin_code):
    binary_list = bin_code.split()
    bytes_data = bytes([int(b, 2) for b in binary_list]).decode('cp1251')
    return bytes_data

def FindSum(encoded_word, open_key):
    sum = []
    for sym in encoded_word:
        for index, num in enumerate(sym):
            if num == 1:
                sum.append(open_key[index])
    return sum

OPEN_KEY = CreateOpenKey(CLOSED_KEY, n, m)
print(OPEN_KEY)
n1 = FindN1(n, m)
print(n1)
encoded_word = EncodeWord('Привет')
print(encoded_word)
sum = FindSum(encoded_word, OPEN_KEY)
print(sum)
decoded_word = DecodeWord(encoded_word)
print(decoded_word)
