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

def main(args:List[str]) -> int:
    interactive_sum_empty()

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)