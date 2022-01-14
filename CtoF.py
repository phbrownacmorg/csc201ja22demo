# Program to read a Celsius temperature
# from the keyboard and print the Fahrenheit
# equivalent

from typing import List

def CtoF(degC:float) -> float:
    return degC * (9/5) + 32

def main(args:List[str]) -> int:
    # Read the Celsius temperature
    degC:float = float(input("Please enter a temperature in Celsius: "))
    print(degC, 'degrees Celsius =', end=' ')

    # deg F = (degC * (9/5)) + 32
    #degF:float = degC * (9/5) + 32

    # Print out the result
    print(CtoF(degC), "degrees Fahrenheit.")

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)