from typing import List

def main(args:List[str]) -> int:
    # Do nothing, successfully

    value:str = 'Hello!'
    value2:str = "My name is I\u00f1igo Montoya."
    value3:str = '''You killed my father.  Prepare to die.'''

    print(value, value2, value3)
    # Concatenated together
    print(value + ' ' + value2 + ' ' + value3) # Spaces have to be added

    # Repetition
    print((value + ' ' + value2 + ' ') * 3)
    print(2 * (value + ' ' + value2 + ' '))

    # len() function
    print(value, len(value))
    print(value2, len(value2))
    print(value3, len(value3))

    # Iteration by character
    print(' ', end='') # Space at the start to line things up
    for c in value:
        print(c, end='  ')
    print()

    # Iteration by index
    print(' ', end='') # Space at the start to line things up
    for i in range(len(value)):
        print(value[i], end='  ')
    print()
    print(' ', end='') # Space at the start to line things up
    for i in range(len(value)):
        print(i, end='  ')
    print()
    
    # Iteration by index from the end
    print(' ', end='') # Space at the start to line things up
    for i in range(-len(value), 0):
        print(value[i], end='  ')
    print()
    for i in range(-len(value), 0):
        print(i, end=' ')
    print()
    
    # Slicing
    for i in range(len(value)+1):
        # Slice up to i, i, slice from i to end
        print(value[:i], i, value[i:])

    # Slicing from the middle
    for i in range(len(value)-2):
        # i, slice up to i, slice from i with length 3, slice from i+3 to the end
        print(i, value[:i], value[i:i+3], value[i+3:])

    # Slicing from the middle using a negative index
    for i in range(-4, -len(value) - 1, -1):
        print(i, value[:i], value[i:i+3], value[i+3:])


    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)