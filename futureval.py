# Program to read a principal value, an
# interest rate, and a number of periods
# from the keyboard, and print out the 
# value of the asset as the interest 
# compounds.

from typing import List

def main(args:List[str]) -> int:
    # Get the input
    # Principal
    P:float = float(input('Please enter an amount to invest: $'))
    # Interest rate, in percent
    rate:float = float(input('Please enter the interest rate, per period: '))
    # Number of compounding periods to invest for
    periods:int = int(input('Please enter the number of periods to invest for: '))

    print('Investing $', P, 'at', rate, '% for', periods, 'periods:')

    # Convert rate from percent to absolute
    rate = rate / 100

    print('\nPeriod\tInterest\tFinal value')
    print('-' * 31)
    print('Initial\t\t\t\t$' + str(P))

    for i in range(periods):
        interest:float = P * rate
        P = P + interest
        print(str(i+1) + '\t\t$' + str(round(interest, 2)) + '\t\t$' + str(round(P, 2)))

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)