# Program to read a principal value, an
# interest rate, and a number of periods
# from the keyboard, and print out the 
# value of the asset as the interest 
# compounds.

from typing import List


def calcValues(P:float, rate:float, periods:int) -> List[float]:
    # Calculate the growth of the investment

    # Convert rate from percent to absolute
    rate = rate / 100
    values:List[float] = [P]

    # Loop to accumulate the answer into the accumulator variable
    for i in range(periods): # type: int
        interest:float = P * rate
        # Update the accumulator variable
        P = P + interest
        values.append(P)

    return values


def printTable(values:List[float]) -> None:
    print('\nPeriod\t\tFinal value')
    print('-' * 23)

    print('Initial\t\t${0:9.2f}'.format(values[0]))
    for i in range(1, len(values)):
        print('{0:^7d}\t\t${1:9.2f}'.format(i, values[i]))


def main(args:List[str]) -> int:
    # Get the input
    # Principal: accumulator variable
    P:float = float(input('Please enter an amount to invest: $'))
    # Interest rate, in percent
    rate:float = float(input('Please enter the interest rate, per period: '))
    # Number of compounding periods to invest for
    periods:int = int(input('Please enter the number of periods to invest for: '))
    print('Investing $', P, 'at', rate, '% for', periods, 'periods:')

    values:List[float] = calcValues(P, rate, periods)
    printTable(values)

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)