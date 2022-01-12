from typing import List

def main(args:List[str]) -> int:
    # Phone number
    intl:str = '+1'
    area:str = '864'
    exchange:str = '867'
    number:str = '5309' # Yes, it's Jenny
    print('7 digits:\t\t\t\t{2}-{3}'.format(intl, area, exchange, number))
    print('10 digits, old style:\t({1}) {2}-{3}'.format(intl, area, exchange, number))
    print('10 digits, more recent:\t{1}-{2}-{3}'.format(intl, area, exchange, number))
    print('10 digits, with dots:\t{1}.{2}.{3}'.format(intl, area, exchange, number))
    print('International:\t\t\t{0} {1}-{2}-{3}'.format(intl, area, exchange, number))

    # SSN
    ssn:str = '123456789'
    print('\nSSN: {0}-{1}-{2}'.format(ssn[:3], ssn[3:5], ssn[5:]))

    # Dates
    monthNames:List[str] = ['', 'January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
    month:int = 1
    day:int = 12
    year:int = 2022

    print('\nUS numeric: {0}/{1}/{2}'.format(month, day, year, monthNames[month]))
    print('British numeric: {1}/{0}/{2}'.format(month, day, year, monthNames[month]))
    print('European numeric: {1}.{0}.{2}'.format(month, day, year, monthNames[month]))
    print('ISO-8601: {2}-{1:02d}-{0:02d}'.format(month, day, year, monthNames[month]))
    print('DOS: {1}-{3}-{2}'.format(month, day, year % 100, monthNames[month][:3]))
    print('US long form: {3} {1}, {2}'.format(month, day, year, monthNames[month]))
    print('British long form: {1} {3} {2}'.format(month, day, year, monthNames[month]))
    print('US short form: {3}. {1}, {2}'.format(month, day, year, monthNames[month][:3]))

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)