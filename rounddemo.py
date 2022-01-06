from typing import List
import math

def main(args:List[str]) -> int:
    # Rounding with round()
    print('\u03c0 =', math.pi)
    print('round(\u03c0) =', round(math.pi))
    print('round(\u03c0, 2) =', round(math.pi, 2))
    print('round(\u03c0, 4) =', round(math.pi, 4))

    # math.ceil() always rounds up
    print('math.ceil(\u03c0) =', math.ceil(math.pi))
    print('math.ceil(-\u03c0) =', math.ceil(-math.pi))

    # math.floor() always rounds down
    print('math.floor(\u03c0) =', math.floor(math.pi))
    print('math.floor(-\u03c0) =', math.floor(-math.pi))

    # int() just throws away the fractional part
    print('int(\u03c0) =', int(math.pi))
    print('int(\u03c0) =', int(-math.pi))

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)