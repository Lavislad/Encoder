class Word():
    def __init__(self, word):
        self.word = word

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