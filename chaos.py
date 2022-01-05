# File: chaos.py
# A simple program illustrating chaotic behavior

def main():
    print("This program illustrates a chaotic function.")
    # Accumulator variable
    x = float(input("Enter a number between 0 and 1: "))
    # Loop in which the answer is accumulated in the accumulator variable
    for i in range(10):
        # Accumulator variable gets updated
        x = 3.9 * x * (1 - x)
        print(x)

if __name__ == "__main__":
    main()
