from graphics import *
from typing import List

def main(args:List[str]) -> int:
    # Do nothing, graphically
    win:GraphWin = GraphWin('Triangle', 200, 200)
    win.setCoords(-1, -1, 1, 1)

    # Display instructions
    instructions:Text = Text(Point(0, 0.8), 'Click to set a point')
    instructions.draw(win)

    # Accumulate points to draw triangle
    pts:List[Point] = [] # Accumulator variable
    for i in range(3):   # Loop
        pt:Point = win.getMouse()
        pt.draw(win)
        pts.append(pt)   # Update the accumulator variable

    poly:Polygon = Polygon(pts)
    poly.draw(win)
    instructions.setText('Click again to exit')

    # Wait for a mouse click
    win.getMouse()
    win.close()

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)