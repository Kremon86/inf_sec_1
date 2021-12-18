def hash_func(num):
    new_hash = 0
    for i, bit in enumerate(bin(num)[2:], start=1):
        new_hash += int(int(bit) + (i**(i*int(bit))) + int(bit)*i**4)
    return hex(new_hash).upper()[2:]


def main():
    hashes = {}
    for num in range(100000):
        hash_num = hash_func(num)
        print()
        print(num, hash_num)
        if hash_num in hashes.values():
            return 'Error'

        hashes[num] = hash_num

    return hashes


if __name__ == '__main__':
    number = int(input('Введите число: '))
    print(hash_func(number))
    print(main())
