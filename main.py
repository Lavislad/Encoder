from lib import *


n = 7
m = 435
CLOSED_KEY = [1, 3, 5, 12, 25, 52, 115, 220]

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
table = make_table_of_encoding_word(word, encoded_word, sum, ciph)
print(table)

# class Class():
#     def __init__(self, arg):
#         self.arg = arg
#
#     def print_a(self):
#         print(self.arg)
# a = Class(1)
# a.print_a()

