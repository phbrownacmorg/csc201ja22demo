from graphics import *
from typing import List

def main(args:List[str]) -> int:
    # Do nothing, graphically
    win:GraphWin = GraphWin('Click to close', 200, 200)

    # Wait for a mouse click
    win.getMouse()
    win.close()

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)