from typing import List

def main(args:List[str]) -> int:
    # Do nothing, successfully

    name:str = input('Please enter your full name as last name, first name: ')
    print('The name you entered was "' + name + '".')

    # Remove white space from the ends
    name = name.strip()
    # Split on the comma to isolate the last name
    parts:List[str] = name.split(',')
    last:str = parts[0]
    firstmiddle:str = parts[1]

    # Get rid of any spaces in the last name
    last = last.replace(' ', '')

    # Split apart first name and middle name(s).  Split on spaces.
    parts = firstmiddle.split()
    first = parts[0]
    middle = ''
    if len(parts) > 1: # If there is a middle name
        middle = parts[1]

    if middle == '':
        userid = first[0] + last
    else:
        userid = first[0] + middle[0] + last
    userid = userid.lower() + '001'

    print('The corresponding userid is "' + userid + '".')

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)