def main():
    g = 3
    p = 17
    Bob = []
    Alisa = []
    Eva = []

    # Расчёт числа Боба и передача Алисе
    Bob.append(g ** 15 % p)
    Alisa.append(g ** 15 % p)
    Eva.append(g ** 15 % p)

    # Расчёт числа Алисф и передача Бобу
    Bob.append(g ** 13 % p)
    Alisa.append(g ** 13 % p)
    Eva.append(g ** 13 % p)

    # Расчёт секретного ключа
    Bob.append(Bob[1] ** 15 % p)
    Alisa.append(Alisa[0] ** 13 % p)

    print('Bob: ', Bob)
    print('Alisa: ', Alisa)
    print('Eva: ', Eva)

    return Alisa[2]


if __name__ == '__main__':
    print('Секретный ключ: ', main())
