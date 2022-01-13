# File: chaos.py
# A simple program illustrating chaotic behavior

def main():
    with open('chaos-seeds.txt', 'r') as infile:
        for line in infile.readlines():
            # Accumulator variable (seed)
            x = float(line)
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

if __name__ == "__main__":
    main()
