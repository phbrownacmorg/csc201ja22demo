from typing import List

# Sum a list of numbers, using the accumulator pattern
def sumlist(args:List[str]) -> int:
    numlist:List[float] = eval(input('Please enter a list of numbers: '))
    print('The list is', numlist)

    # Accumulator variable.
    # The initial value depends on how you're accumulating.
    # Normally, it will be the identity element of the accumulating operation.
    total:float = 0

    # Loop to accumulate the answer into the accumulator variable
    for num in numlist: # type: float
        # Update the accumulator variable
        total = total + num

    # Print the result
    print('The sum of the list is', total)

    # Conventional return value indicating successful completion
    return 0

# Find the product of a list of numbers, using the accumulator pattern
def list_product(args:List[str]) -> int:
    numlist:List[float] = eval(input('Please enter a list of numbers: '))
    print('The list is', numlist)

    # Accumulator variable.
    # The initial value depends on how you're accumulating.
    # Normally, it will be the identity element of the accumulating operation.
    product:float = 1

    # Loop to accumulate the answer into the accumulator variable
    for num in numlist: # type: float
        # Update the accumulator variable
        product = product * num

    # Print the result
    print('The product of the list is', product)

    # Conventional return value indicating successful completion
    return 0

# Find the factorial of a positive integer n, using the accumulator pattern
def factorial(args:List[str]) -> int:
    n:int = int(input('Please enter a positive integer: '))
    print(str(n) + '! = ', end='')

    # Accumulator variable.
    # The initial value depends on how you're accumulating.
    # Normally, it will be the identity element of the accumulating operation.
    product:float = 1

    # Loop to accumulate the answer into the accumulator variable
    for i in range(1, n+1): # Numbers from 1 up to and including n
        # Update the accumulator variable
        product = product * i

    # Print the result
    print(product)

    # Conventional return value indicating successful completion
    return 0

def two_accumulator_variables(args:List[str]) -> int:
    numlist:List[float] = eval(input('Please enter a list of numbers: '))
    print('The list is', numlist)

    # Accumulator variable #1
    # The initial value depends on how you're accumulating.
    # Normally, it will be the identity element of the accumulating operation.
    total:float = 0
    # Accumulator variable #2
    product:float = 1

    # Loop to accumulate the answer into the accumulator variable(s)
    for num in numlist: # type: float
        # Update accumulator variable #1
        total = total + num
        # Update accumulator variable #2
        product = product * num

    # Print the results
    print('The sum of the list is', total)
    print('The product of the list is', product)

    # Conventional return value indicating successful completion
    return 0

def main(args:List[str]) -> int:
    # Make a table of the first 128 Unicode characters

    # Start with the column headers
    # table is the accumulator variable
    table:str = 'Number\tCharacter\n'
    table = table + ('-'  * 20)

    # Accumulator loop (add a row to the table each time)
    for i in range(33, 256):
        # Update the accumulator variable
        table = table + '\n' + str(i) + '\t\t' + chr(i)

    print(table)

    # Conventional return value indicating successful completion
    return 0



if __name__ == '__main__':
    import sys
    main(sys.argv)