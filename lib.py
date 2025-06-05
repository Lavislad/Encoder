class Word():
    def __init__(self, word):
        self.word = word

    def encode_word(self):
        bytes_data = self.word.encode('cp1251')
        binary_str = ' '.join(format(byte, '08b') for byte in bytes_data)
        return binary_str

    def make_list_of_word(self):
        result = []
        for sym in self.word:
            result.append(sym)
        return result

    def find_sum(self, open_key):
        total = {}
        encoded_word_list = self.word.split()
        print(f'encoded_word_list: {encoded_word_list}')
        for encoded_sym in encoded_word_list:
            total[f'{encoded_sym}'] = []
            for index, num in enumerate(encoded_sym):
                if num == '1':
                    total[encoded_sym].append(open_key[index])
        return total

    def FindCiphergram(self, dict):
        total = {}
        for encoded_sym in dict:
            total[encoded_sym] = 0
            for num in dict[encoded_sym]:
                total[encoded_sym] += num
        return total