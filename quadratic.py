from typing import List, Tuple
import math

def det(a:float, b:float, c:float) -> float:
    return b**2 - 4*a*c

def roots(a:float, b:float, c:float) -> Tuple[float, float]:
    root1:float = (-b + math.sqrt(det(a, b, c))) / 2*a
    root2:float = (-b - math.sqrt(det(a, b, c))) / 2*a
    return root1, root2

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

    root1, root2 = roots(a, b, c) # type: Tuple[float, float]
    print('\t', root1, 'and', root2)

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)