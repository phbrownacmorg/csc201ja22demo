from typing import List

def main(args:List[str]) -> int:
    with open('namegenerator.csv','r') as infile:
        with open('userids.csv','w') as outfile:
            for line in infile.readlines()[1:]: # All but first line
                # Get the parts
                parts:List[str] = line.split(',')
                last:str = parts[1].strip().lower()
                first:str = parts[2].strip().lower()
                middle:str = parts[3].strip().lower()

                # Remove unwanted characters in the last name
                last = last.replace(' ', '')
                last = last.replace("'", '')

                # Make the userid from the parts.  Slicing is
                # used on the first and middle names to handle
                # the case where either or both of these may not
                # exist (may just be the empty string).
                userid:str = first[:1] + middle[:1] + last + '001'
                outfile.write('{0},{1},{2},{3}\n'.format(userid, last,
                        first,middle))

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)