from collections import Counter
from Laba1_1 import calc_cipher
from itertools import islice
import re


def get_caesar_cipher(message):
    A = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ \n'

    f = {char: 0 for char in A}
    with open('st.txt', encoding='utf-8') as file:
        for line in file:
            for char in line:
                char = char.upper()
                if char != ' ':
                    char = char.upper()
                    if char in f.keys():
                        f[char] += 1
                    else:
                        f[char] = 1

    result = []
    letters = [' ', 'О', 'А', 'Е', 'И', 'Е', 'Н', 'Л',
               'Р', 'С', 'В', 'К', 'М', 'Д', 'У', 'П',
               'Б', 'Г', 'T', 'Ы', 'Ч', 'Ь', 'З', 'Я', 'Й',
               'Х', 'Ж', 'Ш', 'Ю', 'Ф', 'Э', 'Щ',
               'Ё', 'Ц', 'Ъ', '\n']

    dictionary = dict(zip(f, letters))
    for i in message:
        if i in letters:
            result.append(dictionary.get(i))
            result.append(i)

    return ''.join(result)


def get_bigram(message, text):
    t = re.findall("\w{2}", text)
    bigr = Counter(islice(t, 1, None))
    print(bigr)
    t = re.findall("\w{2}", message)
    s_bigr = Counter(islice(t, 1, None))
    for i, y in zip(s_bigr.most_common(), bigr.most_common()):
        message = message.replace(i[0], y[0])

    return message


def get_text(file_name):
    with open(file_name, encoding='utf-8') as file:
        result = ''
        for line in file:
            result += line

        return result


def main():
    text = get_text('text.txt')
    text = text.upper()
    print(text)
    print('\n\n\n\n')
    result = calc_cipher(text, 6)
    print('\n\n\n\n')
    print(result)
    c = get_caesar_cipher(result)
    print('\n\n\n\n')
    print(c)
    print('\n\n\n\n')
    return get_bigram(result, text)


if __name__ == '__main__':
    print(main())
