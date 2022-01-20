# Program to read a principal value, an
# interest rate, and a number of periods
# from the keyboard, and print out the 
# value of the asset as the interest 
# compounds.

from graphics import *
import math
import sys
from typing import List, Tuple

def readInt(prompt:str) -> int:
    # Read an integer from the keyboard, checking to
    # make sure it's a valid integer.  If it's *not*
    # a valid integer, return -sys.maxsize.  (This
    # function should not crash on invalid input.)
    inString:str = input(prompt).strip()
    # Now, I should have an optional negative sign
    # followed by one or more digits.
    validInt:bool = inString.isdigit() or \
        (inString[0] == '-' and inString[1:].isdigit())
    if validInt:
        return int(inString)
    else:
        print('Input "' + inString + '" is not a valid integer.')
        return -sys.maxsize

def readFloat(prompt:str) -> float:
    # Read a float from the keyboard, checking to see whether
    # it's a valid floating-point number.  This should not
    # crash if an invalid float is entered.  Instead, it
    # should return math.nan.
    # To simplify things, this function does not support
    # exponential or scientific notation for a float.
    inString:str = input(prompt).strip()
    testStr:str = inString[:]
    # Optional minus sign
    if testStr[0] == '-':
        testStr = testStr[1:]
    # Remove up to one decimal point (but no more)
    testStr = testStr.replace('.', '', 1)
    # Now, there should be nothing here but digits
    if testStr.isdigit():
        return float(inString)
    else:
        print('Input "' + inString + '" is not a valid floating-point number.')
        return math.nan

def readInput() -> Tuple[float, float, int]:
    # Principal: accumulator variable
    P:float = readFloat('Please enter an amount to invest: $')
    # Validate the principal
    if not (P > 0): # math.nan is not > 0
        print('Principal should be greater than 0.')
        P = math.nan
        return P, 0, 0

    # Interest rate, in percent
    rate:float = readFloat('Please enter the interest rate, per period: ')
    # Validate the rate
    if not (rate > 0):
        print('Interest rate must be greater than 0.')
        rate = math.nan
        return P, rate, 0

    # Number of compounding periods to invest for
    periods:int = readInt('Please enter the number of periods to invest for: ')
    # Validate the periods
    if (periods <= 0):
        print('Number of periods must be greater than 0.')
        periods = 0
        # No need for a special return statement
    return P, rate, periods # Python turns these into a tuple

def validInput(P:float, rate:float, periods:int) -> bool:
    return (P > 0) and (rate > 0) and (periods > 0)

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
    P, rate, periods = readInput() # type: float, float, int
    # Validation
    if not validInput(P, rate, periods):
        print('Invalid input.  Exiting.')
        return 0
    print('Investing $', P, 'at', rate, '% for', periods, 'periods:')

    values:List[float] = calcValues(P, rate, periods)
    printTable(values)
    graphTable(values)

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)