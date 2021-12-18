import random
from Practica_1 import isPrime
from math import gcd


def get_rand_prime(num):
    prime = []

    for number in range(1, num + 1):
        if isPrime(number, 4):
            prime.append(number)

    return prime[random.randint(1, len(prime) - 1)]


def main():
    Bob = []
    Alisa = []
    Eva = []
    g = get_rand_prime(10000)
    p = get_rand_prime(10000)
    n = p * g
    f_e = (p-1) * (g - 1)

    while True:
        i = random.randint(2, f_e - 1)
        if gcd(i, f_e) == 1:
            e = i
            break

    while (f_e * i + 1) % e != 0:
        i += 1
    d = (f_e * i + 1) // e
    print('Открытый ключ: ', e, n)
    print('Закрытый ключ: ', d, n)

    m = 11111
    Alisa.append(m)
    c = m**e % n

    Bob.append(c)
    Alisa.append(c)
    Eva.append(c)
    print("Alisa: ", Alisa)
    print("Bob: ", Bob)
    print("Eva: ", Eva)

    m = c**d % n

    Bob.append(m)
    print("Alisa: ", Alisa)
    print("Bob: ", Bob)
    print("Eva: ", Eva)

    print('Шифрованное сообщение: ', Bob[-1])


if __name__ == '__main__':
    main()
