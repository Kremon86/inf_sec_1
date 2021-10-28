def calc_cipher(message, step):
    A = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ''
    message = message.upper()
    for i in message:
        char = A.find(i)
        new_char = char + step
        if i in A:
            result += A[new_char]
        else:
            result += i

    return result


if '__main__' == __name__:
    s = int(input('Шаг шифровки: '))
    mes = input("Сообщение для шифровки: ").upper()
    print(calc_cipher(mes, s))
