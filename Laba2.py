from random import randint


def main():
    g = randint(10, 10000)
    p = randint(10, 10000)

    a = randint(10, 10000)
    b = randint(10, 10000)

    Bob = [g, p]
    Alisa = [g, p]
    Eva = [g, p]

    Bob.append(g ** a % p)
    Alisa.append(g ** a % p)
    Eva.append(g ** a % p)

    Bob.append(g ** b % p)
    Alisa.append(g ** b % p)
    Eva.append(g ** b % p)

    Bob.append(Bob[-2] ** b % p)
    Alisa.append(Alisa[-1] ** a % p)

    print('Bob: ', Bob)
    print('Alisa: ', Alisa)
    print('Eva: ', Eva)

    return Alisa[-1]


if __name__ == '__main__':
    print('Секретный ключ: ', main())
