# File: chaos.py
# A simple program illustrating chaotic behavior

from typing import List

def readSeeds(fname:str) -> List[float]:
    seedList:List[float] = []
    with open(fname, 'r') as infile:
        linenum = 0
        for line in infile.readlines():
            linenum = linenum + 1
            # Accumulator variable (seed)
            try:
                x = float(line)
            except ValueError as e:
                raise ValueError('Input line {0}: seed {1} must be a floating-point number.'.format(linenum, line.strip()))
            if (x < 0) or (x > 1):
                raise ValueError('Input line {0}: seed must be between 0 and 1.'.format(linenum))
            seedList.append(x)
    return seedList

def writeChaos(seeds:List[float], fname:str) -> None:
    for x in seeds:
       print(x)
       with open('chaos-out.txt', 'a') as outfile:
            outfile.write('seed = {0}\n'.format(x))
            outfile.write('{0:^3}\t\t{1:^9}\n'.format('i', 'x'))
            outfile.write(('-' * 20) + '\n')
            for i in range(5):
                # Accumulator variable gets updated
                x = 3.9 * x * (1 - x)
                outfile.write('{0:>3}\t\t{1:0.7f}\n'.format(i,x))
            outfile.write('\n')

def main() -> int:
    infilename:str = 'chaos-seeds.txt'
    try:        
        seeds:List[float] = readSeeds(infilename)
        writeChaos(seeds, 'chaos-out.txt')
    except ValueError as e:
        print(e)
    except FileNotFoundError as e:
        print('File', infilename, 'could not be found.')

    return 0

if __name__ == "__main__":
    main()
