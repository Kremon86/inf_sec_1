import random
from Practica_1 import isPrime


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
    g = random.randint(100, 10000)
    Bob.append(g)
    Alisa.append(g)
    Eva.append(g)
    print("Alisa : ", Alisa)
    print("Bob: ", Bob)
    print("Eva: ", Eva)

    p = random.randint(100, 10000)
    Bob.append(p)
    Alisa.append(p)
    Eva.append(p)
    print("Alisa: ", Alisa)
    print("Bob: ", Bob)
    print("Eva: ", Eva)

    Alisa_gen = get_rand_prime(10000)
    Alisa.append(Alisa_gen)
    print("Alisa: ", Alisa)
    Alisa_gen = g ** Alisa_gen % p
    Bob.append(Alisa_gen)
    Alisa.append(Alisa_gen)
    Eva.append(Alisa_gen)
    print("Alisa: ", Alisa)
    print("Bob: ", Bob)
    print("Eva: ", Eva)

    Bob_gen = get_rand_prime(10000)
    Bob.append(Bob_gen)
    print("Bob: ", Bob)
    Bob_gen = g ** Bob_gen % p
    Bob.append(Bob_gen)
    Alisa.append(Bob_gen)
    Eva.append(Bob_gen)
    print("Alisa: ", Alisa)
    print("Bob: ", Bob)
    print("Eva: ", Eva)

    Alisa.append(Alisa[-1] ** Alisa[-3] % p)
    Bob.append(Bob[-3] ** Bob[-2] % p)
    print("Alisa: ", Alisa)
    print("Bob: ", Bob)
    print("Eva: ", Eva)

    print('Шифрованное сообщение: ', Alisa[-1])
    print('Eva не знает простых чисел Alisa и Bob, чтобы расшифровать сообщение')

if __name__ == '__main__':
    main()