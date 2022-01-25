# Program to read a principal value, an
# interest rate, and a number of periods
# from the keyboard, and print out the 
# value of the asset as the interest 
# compounds.

import math
import sys
from typing import List, Tuple

# Read a list of investments from a file.  Each investment
# consists pf a principal value, interest rate, and number of periods.
def getParameters(infilename:str) -> List[Tuple[float, float, int]]:
    paramsList:List[Tuple[float, float, int]] = []
    with open(infilename, 'r') as f:
        for line in f.readlines():
            cleaned_line:str = line.replace('$', '').replace('%', '')
            parts:List[str] = cleaned_line.split()
            P:float = float(parts[0])
            rate:float = float(parts[1])
            periods:int = int(parts[2])
            paramsList.append((P, rate, periods))
    return paramsList

def calcValues(P:float, rate:float, periods:int) -> List[float]:
    # Calculate the growth of the investment, and return the resulting list of values

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

def writeTable(values:List[float], outfilename:str) -> None:
    with open(outfilename, 'a') as f:
        rate:float = ((values[1] / values[0]) - 1.0) * 100
        f.write('Investing ${0:.2f} at {1:.2f}% for {2} periods:\n'.format(values[0],
                rate, len(values) - 1))

        # Print the growth table of the investment to the terminal
        f.write('Period\t\tFinal value\n')
        f.write('-' * 23 + '\n')
        f.write('Initial\t\t${0:9.2f}\n'.format(values[0]))
        for i in range(1, len(values)):
            f.write('{0:^7d}\t\t${1:9.2f}\n'.format(i, values[i]))
        f.write('\n\n')

def main(args:List[str]) -> int:
    # Get the input
    params:List[Tuple[float, float, int]] = getParameters('futureval_in.txt')
    for investment in params: # type: Tuple[float, float, int]
        P, rate, periods = investment # type: float, float, int
        values:List[float] = calcValues(P, rate, periods)
        writeTable(values, 'futureval_out.txt')

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)