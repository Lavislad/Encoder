n = 7
m = 435
CLOSED_KEY = [1, 3, 5, 12, 25, 52, 115, 220]

def CreateOpenKey(closed_key, n, m):
    open_key = []
    for el in closed_key:
        open_key.append(el * n % m)
    return open_key

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

# class Class():
#     def __init__(self, arg):
#         self.arg = arg
#
#     def print_a(self):
#         print(self.arg)
# a = Class(1)
# a.print_a()

