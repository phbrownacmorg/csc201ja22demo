from typing import List

def printVerse(animals:str, noise:str) -> None:
    print('Old MacDonald had a farm,')
    print('E-I-E-I-O!')
    print('And on that farm he had some {0},'.format(animals))
    print('E-I-E-I-O!')
    print('With a {0}, {0} here and a {0}, {0} there,'.format(noise))
    print('Here a {0}, there a {0}, everywhere a {0}, {0},'.format(noise))
    print('Old MacDonald had a farm,')
    print('E-I-E-I-O!')
    print()

def main(args: List[str]) -> int:
    printVerse('chickens', 'cluck')
    printVerse('pigs', 'oink')
    printVerse('cows', 'moo')
    printVerse('sheep', 'baa')
    printVerse('goats', 'bleat')
    printVerse('dogs', 'bark')
    printVerse('cats', 'meow')
    printVerse('horses', 'neigh')
    printVerse('fish', 'glug')

    # Conventional return value indicating successful completion
    return 0


if __name__ == '__main__':
    import sys
    main(sys.argv)
