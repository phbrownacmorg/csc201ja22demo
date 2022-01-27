from typing import List


def eligibleHouse(age:int, citizen:int) -> bool:
    # Return whether a person of the given AGE who has been a U.S. citizen 
    # for the number of years given in CITIZEN is eligible to serve in the
    # U.S. House.
    return (age >= 25) and (citizen >= 7)

def eligibleSenate(age:int, citizen:int) -> bool:
    # Return whether a person of the given AGE who has been a U.S. citizen 
    # for the number of years given in CITIZEN is eligible to serve in the
    # U.S. Senate.
    return (age >= 30) and (citizen >= 9)

def main(args:List[str]) -> int:
    age:int = int(input("Please enter the person's age: "))
    citizen:int = int(input("How long has this person been a U.S. citizen? "))
    print('A person who is {0} years old '.format(age) +
            'and has been a citizen for {0} years'.format(citizen))

    if eligibleHouse(age, citizen): # function call gives values to parameters
        print('\tis eligible to serve in the House of Representatives')
    else:
        print('\tis NOT eligible to serve in the House of Representatives')

    if eligibleSenate(age, citizen): # function call gives values to parameters
        print('\tis eligible to serve in the Senate')
    else:
        print('\tis NOT eligible to serve in the Senate')


    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)