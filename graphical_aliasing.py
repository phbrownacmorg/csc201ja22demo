from graphics import *
from typing import List

def main(args:List[str]) -> int:
    # Do nothing, graphically
    win:GraphWin = GraphWin('Click to close', 200, 200)
    win.setCoords(-1, -1, 1, 1)

    # Create a "mouse" to chase the mouse clicks
    # Start it in center
    rodent:Circle = Circle(Point(0, 0), 0.05)
    rodent.setFill('gray')
    rodent.draw(win)
    rodentPt:Point = rodent.getCenter()
    
    p:Point = win.getMouse()
    rodent2:Circle = rodent.clone()
    rodent2.draw(win)
    dx:float = p.getX() - rodentPt.getX()
    dy:float = p.getY() - rodentPt.getY()
    rodent2.move(dx, dy)
    rodentPt = rodent2.getCenter()

    p = win.getMouse()
    rodent3:Circle = rodent # Aliasing!
    dx:float = p.getX() - rodentPt.getX()
    dy:float = p.getY() - rodentPt.getY()
    rodent3.move(dx, dy)
    rodentPt = rodent3.getCenter()

    # Wait for a mouse click
    win.getMouse()
    win.close()

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)