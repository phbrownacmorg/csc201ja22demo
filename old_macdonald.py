from typing import List

def printVerse(animals:str, noise:str) -> None:
    article:str = 'a'
    if (noise[0] == 'a') or (noise[0] == 'e') or (noise[0] == 'i') or (noise[0] == 'o') or (noise[0] == 'u'):
        article = 'an'

    print('Old MacDonald had a farm,')
    print('E-I-E-I-O!')
    print('And on that farm he had some {0},'.format(animals))
    print('E-I-E-I-O!')
    print('With {1} {0}, {0} here and {1} {0}, {0} there,'.format(noise, article))
    print('Here {1} {0}, there {1} {0}, everywhere {1} {0}, {0},'.format(noise, article))
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
