from typing import List

# Interactive loop (using "Q" or "q" as a sentinel)
def interactive_sum_q() -> None:
    total:float = 0
    count:int = 0

    response:str = input('Please enter a number, or "Q" to quit: ')
    while response.strip().lower() != 'q':
        number:float = float(response)
        count = count + 1
        total = total + number
        print('Seen', count, 'numbers totalling', total, 'and averaging', (total/count))
        response = input('Please enter a number, or "Q" to quit: ')

# Interactive loop (using a negative value as a sentinel)
def interactive_sum_neg() -> None:
    total:float = 0
    count:int = 0

    number:float = float(input('Please enter a number, or a negative number to quit: '))
    while number >= 0:
        count = count + 1
        total = total + number
        print('Seen', count, 'numbers totalling', total, 'and averaging', (total/count))
        number = float(input('Please enter a number, or a negative number to quit: '))

# Interactive loop (using the empty string as a sentinel)
def interactive_sum_empty() -> None:
    total:float = 0
    count:int = 0

    response:str = input('Please enter a number, or just hit Enter to quit: ')
    while response.strip() != '':
        number:float = float(response)
        count = count + 1
        total = total + number
        print('Seen', count, 'numbers totalling', total, 'and averaging', (total/count))
        response = input('Please enter a number, or just hit Enter to quit: ')

# Interactive loop (using exceptions)
def interactive_sum_except() -> None:
    total:float = 0
    count:int = 0

    try:
        while True:
            number:float = float(input('Please enter a number, or anything else to quit: '))
            count = count + 1
            total = total + number
            print('Seen', count, 'numbers totalling', total, 'and averaging', (total/count))
    except ValueError:
        return None

# Sum from a file, the usual way in Python
def sum_from_file_usual(fname:str) -> None:
    total:float = 0
    count:int = 0

    # Usual Python pattern
    with open(fname, 'r') as infile:
        for line in infile.readlines():
            number:float = float(line)
            total = total + number
            count = count + 1
    print('Saw', count, 'numbers totalling', total, 'and averaging', (total/count))

# Sum from a file, in a way common to many languages
def sum_from_file_general(fname:str) -> None:
    total:float = 0
    count:int = 0

    # Usual Python pattern
    with open(fname, 'r') as infile:
        line:str = infile.readline()
        while line != '':
            number:float = float(line)
            total = total + number
            count = count + 1
            line = infile.readline()
    print('Saw', count, 'numbers totalling', total, 'and averaging', (total/count))

def sum_from_file_nested(fname:str) -> None:
    total:float = 0
    count:int = 0

    with open(fname, 'r') as f:
        # Loop
        for line in f.readlines():
            lineparts:List[str] = line.split(',')
            # Loop nested inside the outer loop
            for part in lineparts:
                number:float = float(part)
                total = total + number
                count = count + 1
    print('Saw', count, 'numbers totalling', total, 'and averaging', (total/count))

def main(args:List[str]) -> int:
    sum_from_file_nested('numlist_nested.txt')

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)