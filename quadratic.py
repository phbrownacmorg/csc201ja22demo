from typing import List
import math

def main(args:List[str]) -> int:
    # Do nothing, successfully
    # Read the coefficients
    print('Please enter coefficients for the\nquadratic a*x**2 + b*x + c = 0')
    a:float = float(input('\ta: '))
    b:float = float(input('\tb: '))
    c:float = float(input('\tc: '))

    print('The system ' + str(a) + '*X**2 + ',end='')
    print(str(b) + '*X +',c,'= 0')
    print('has the following roots:')

    det:float = b**2 - 4*a*c
    root1:float = (-b + math.sqrt(det)) / 2*a
    root2:float = (-b - math.sqrt(det)) / 2*a
    print('\t', root1, 'and', root2)

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)