from typing import List

def main(args:List[str]) -> int:
    # Do nothing, successfully
    print('One-argument version of range starts from 0')
    print('and goes up to (but not including) the argument.')
    print('\trange(10):', list(range(10)))

    print('\nTwo-argument version of range starts from the first argument')
    print('and goes up to (but not including) the second argument.')
    print('\trange(4, 10):', list(range(4, 10)))

    print('\nThree-argument version of range starts from the first argument')
    print('and goes to (but not including) the second argument,')
    print('using the third argument as the step size.')
    print('\trange(4, 10, 3):', list(range(4, 10, 3)))

    print('\nThree-argument version used to count down.')
    print('\trange(9, -1, -1):', list(range(9, -1, -1)))
    print('\tThis particular one is the reverse of range(10).')

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)