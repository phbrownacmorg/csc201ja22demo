# Program to read a principal value, an
# interest rate, and a number of periods
# from the keyboard, and print out the 
# value of the asset as the interest 
# compounds.

from graphics import *
import math
import sys
from typing import List, Tuple

def readInput() -> Tuple[float, float]:
    # Principal: accumulator variable
    try:
        P:float = float(input('Please enter an amount to invest: $'))
        if not (P > 0):
            raise ValueError('')
    except ValueError as e:
        raise ValueError('Principal must be a floating-point number greater than 0. Exiting.') from e

    # Interest rate, in percent
    try:
        rate:float = float(input('Please enter the interest rate, per period: '))
        if not (rate > 0):
            raise ValueError('')
    except ValueError as e:
        raise ValueError('Interest rate must be a floating-point number greater than 0. Exiting.') from e

    return P, rate # Python turns these into a tuple

def calcValues(P:float, rate:float) -> List[float]:
    # Calculate the growth of the investment until it doubles, and return the resulting list of values

    # Convert rate from percent to absolute
    rate = rate / 100
    values:List[float] = [P]
    P0:float = P # Initial value of P

    # Loop to accumulate the answer into the accumulator variable
    while P < (2 * P0):
        interest:float = P * rate
        # Update the accumulator variable
        P = P + interest
        values.append(P)

    return values


def printTable(values:List[float]) -> None:
    # Print the growth table of the investment to the terminal
    print('\nPeriod\t\tFinal value')
    print('-' * 23)
    print('Initial\t\t${0:9.2f}'.format(values[0]))
    for i in range(1, len(values)):
        print('{0:^7d}\t\t${1:9.2f}'.format(i, values[i]))

def makeAxis(endPt:Point) -> Line:
    # Create and return an axis from the origin to ENDPT.
    axis:Line = Line(Point(0, 0), endPt)
    axis.setArrow('last')
    return axis

def graphTable(values:List[float]) -> None:
    # Create a window and graph the given VALUES
    w:GraphWin = GraphWin('Asset value', 200, 200)
    
    # Figure out coordinates
    maxX = len(values)
    maxY = max(values)
    borderFactor = 0.15

    w.setCoords(-borderFactor * maxX, -borderFactor * maxY,
                (1+borderFactor) * maxX, (1+borderFactor) * maxY)
    
    # Axes
    makeAxis(Point(maxX * (1+borderFactor/2), 0)).draw(w)
    makeAxis(Point(0, maxY * (1+borderFactor/2))).draw(w)

    # Draw bars
    for i in range(len(values)):
        bar:Rectangle = Rectangle(Point(i,0), Point(i+1,values[i]))
        bar.setFill('green')
        bar.draw(w)

    # Wait for a mouse click
    w.getMouse()
    w.close()

def main(args:List[str]) -> int:
    # Get the input
    try:
        P, rate = readInput() # type: float, float
    except ValueError as e:
        print(e)
    else:
        print('Investing $', P, 'at', rate, '% until P doubles:')

        values:List[float] = calcValues(P, rate)
        printTable(values)
        graphTable(values)

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)