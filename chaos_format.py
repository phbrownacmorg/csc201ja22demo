# File: chaos.py
# A simple program illustrating chaotic behavior

def main():
    print("This program illustrates a chaotic function.")
    # Accumulator variable
    x = float(input("Enter a number between 0 and 1: "))

    # Clamp the input to the range [0, 1]
    x = max(0, min(1, x))

    # Print table headers
    print('{0:^3}\t\t{1:^9}'.format('i', 'x'))
    print('-' * 20)
    # Loop in which the answer is accumulated in the accumulator variable
    for i in range(20):
        # Accumulator variable gets updated
        x = 3.9 * x * (1 - x)
        print('{0:>3}\t\t{1:0.7f}'.format(i,x))

if __name__ == "__main__":
    main()
