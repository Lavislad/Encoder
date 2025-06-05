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
