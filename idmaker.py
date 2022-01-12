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

    userid = last
    # Add on the initials from the first and middle names.
    # Use a loop here because there might not be a middle name!
    initials:str = ''
    for p in parts:
        initials = initials + p.strip()[0]
    userid = (initials + userid).lower() + '001'

    print('The corresponding userid is "' + userid + '".')

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)