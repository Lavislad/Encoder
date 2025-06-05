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
    total = {}
    encoded_word_list = encoded_word.split()
    print(f'encoded_word_list: {encoded_word_list}')
    for encoded_sym in encoded_word_list:
        total[f'{encoded_sym}'] = []
        for index, num in enumerate(encoded_sym):
            if num == '1':
                total[encoded_sym].append(open_key[index])
    return total

def FindCiphergram(dict):
    total = {}
    for encoded_sym in dict:
        total[encoded_sym] = 0
        for num in dict[encoded_sym]:
            total[encoded_sym] += num
    return total


OPEN_KEY = CreateOpenKey(CLOSED_KEY, n, m)
print(OPEN_KEY)
n1 = FindN1(n, m)
print(n1)
encoded_word = EncodeWord('Привет')
print(encoded_word)
total = FindSum(encoded_word, OPEN_KEY)
print(total)
sum_ciph = FindCiphergram(total)
print(sum_ciph)
decoded_word = DecodeWord(encoded_word)
print(decoded_word)
