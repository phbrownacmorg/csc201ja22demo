# Basic mouse interaction

from graphics import *
from typing import List

def main(args:List[str]) -> int:
    # Do nothing, graphically
    win:GraphWin = GraphWin('Click to close', 300, 300)
    win.setCoords(-1, -1, 1, 1)

    # Create a "mouse" to chase the mouse clicks
    # Initially off the screen
    rodent:Circle = Circle(Point(2, 0), 0.1)
    rodent.setFill('gray')
    rodent.draw(win)
    rodentPt:Point = rodent.getCenter()

    # Collect mouse clicks
    for i in range(5):
        p:Point = win.getMouse()
        dx:float = p.getX() - rodentPt.getX()
        dy:float = p.getY() - rodentPt.getY()
        rodent.move(dx, dy)
        rodentPt = rodent.getCenter()

    # Wait for a mouse click
    win.getMouse()
    win.close()

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)