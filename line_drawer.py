from graphics import *
from typing import List
import math

def main(args:List[str]) -> int:
    # Do nothing, graphically
    win:GraphWin = GraphWin('Draw a line', 200, 200)
    win.setCoords(-1, -1, 1, 1)

    instructions:Text = Text(Point(0, .75), 'Click to set one end of a line')
    instructions.setSize(10)
    instructions.draw(win)

    p1:Point = win.getMouse()
    p1.draw(win)
    instructions.setText('Click again for the other end')

    p2:Point = win.getMouse()
    p2.draw(win)
    line:Line = Line(p1, p2)
    line.draw(win)
    instructions.setText('Click again to exit')

    # Find and display the length of the line
    length:float = math.sqrt((p1.getX() - p2.getX())**2 + (p1.getY() - p2.getY())**2)
    lengthLabel:Text = Text(Point(0, -.75), 
        'p1: ({1:7.4f}, {2:7.4f})\np2: ({3:7.4f}, {4:7.4f})\nLength: {0:0.4f}'.format(length,
            p1.getX(), p1.getY(), p2.getX(), p2.getY()))
    lengthLabel.setSize(10)
    lengthLabel.draw(win)

    # Wait for a mouse click
    win.getMouse()
    win.close()

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)