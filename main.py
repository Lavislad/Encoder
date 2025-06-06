from lib import Word
from tabulate import tabulate


n = 7
m = 435
CLOSED_KEY = [1, 3, 5, 12, 25, 52, 115, 220]

def create_open_key(closed_key, n, m):
    open_key = []
    for el in closed_key:
        open_key.append(el * n % m)
    return open_key

def find_n1(n, m):
    n1 = 1
    success = False
    while success is False:
        if (n*n1)%m == 1:
            success = True
        else:
            n1+=1
    return n1

def decode_word(word):
    binary_list = word.split()
    bytes_data = bytes([int(b, 2) for b in binary_list]).decode('cp1251')
    return bytes_data

def find_sum(word, open_key):
    total = {}
    encoded_word_list = word.split()
    print(f'encoded_word_list: {encoded_word_list}')
    for encoded_sym in encoded_word_list:
        total[f'{encoded_sym}'] = []
        for index, num in enumerate(encoded_sym):
            if num == '1':
                total[encoded_sym].append(open_key[index])
    return total

def find_ciphergram(dict):
    total = {}
    for encoded_sym in dict:
        total[encoded_sym] = 0
        for num in dict[encoded_sym]:
            total[encoded_sym] += num
    return total

def make_table_of_word(word, encoded_word, sum_dict, ciphergram):
    data = []
    list_of_word = word.make_list_of_word()
    encoded_word_list = encoded_word.split()
    for index in range(len(list_of_word)):
        row = []
        row.append(list_of_word[index])
        row.append(encoded_word_list[index])
        row.append(sum_dict[encoded_word_list[index]])
        row.append(ciphergram[encoded_word_list[index]])
        data.append(row)
    headers = ['Symbol', 'Bin code', 'Sum', 'Ciphergram']
    return tabulate(data, headers=headers, tablefmt='grid')


word = Word('Привет')
print(word.make_list_of_word())
encoded_word = word.encode_word()
print(encoded_word)
OPEN_KEY = create_open_key(CLOSED_KEY, n, m)
sum = find_sum(encoded_word, OPEN_KEY)
print(f'sum: {sum}')
ciph = find_ciphergram(sum)
print(ciph)
print(decode_word(encoded_word))
table = make_table_of_word(word, encoded_word, sum, ciph)
print(table)

# print(OPEN_KEY)
# n1 = find_n1(n, m)
# print(n1)
# encoded_word = EncodeWord('Привет')
# print(encoded_word)
# total = find_sum(encoded_word, OPEN_KEY)
# print(total)
# sum_ciph = find_ciphergram(total)
# print(sum_ciph)
# decoded_word = decode_word(encoded_word)
# print(decoded_word)

# class Class():
#     def __init__(self, arg):
#         self.arg = arg
#
#     def print_a(self):
#         print(self.arg)
# a = Class(1)
# a.print_a()

