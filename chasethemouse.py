# Basic mouse interaction

from graphics import *
import math
from typing import List

def main(args:List[str]) -> int:
    # Do nothing, graphically
    win:GraphWin = GraphWin('Click to close', 300, 300)
    win.setCoords(-1, -1, 1, 1)

    # Create a "mouse" to chase the mouse clicks
    # Initially off the screen
    rodentPt:Point = Point(2, 0)
    radius:float = 0.05
    rodent:List[GraphicsObject] = [] # Empty list
    head:Circle = Circle(Point(0, 0), radius)
    head.setFill('gray')
    head.setOutline('gray')
    rodent.append(head)

    # Ears
    for i in range(2):
        angle = (math.pi/3) + i * (math.pi/3)
        earPt:Point = Point(1.3 * radius * math.cos(angle),
                            1.3 * radius * math.sin(angle))
        ear:Circle = Circle(earPt, radius * .5)
        ear.setFill('gray')
        ear.setOutline('gray')
        rodent.append(ear)

    # Eyes
    for i in range(2):
        angle:float = math.radians(50) + i * math.radians(80)
        lowerPt:Point = Point(0, radius * -0.2)
        upperPt:Point = Point(radius * math.cos(angle),
                              radius * math.sin(angle))
        eye:Oval = Oval(lowerPt, upperPt)
        eye.setFill('black')
        rodent.append(eye)

    # Mouth
    # BROKEN. The side of the mouth with i == 1 is bigger than the side with i == 0.
    for i in range(2):
        meeting:Point = Point(0, -0.35 * radius)
        angle = math.radians(330) - i * math.radians(120)
        endPt:Point = Point(meeting.getX() + 0.5 * radius * math.cos(angle),
                            meeting.getY() + 0.5 * radius * math.sin(angle))
        mouthPart:Line = Line(meeting, endPt)
        rodent.append(mouthPart)

    # Everything's a GraphicsObject, even though they're not all the same
    for mousePart in rodent:
        mousePart.move(rodentPt.getX(), rodentPt.getY())
        mousePart.draw(win)
    

    # Collect mouse clicks
    for i in range(5):
        p:Point = win.getMouse()
        dx:float = p.getX() - rodentPt.getX()
        dy:float = p.getY() - rodentPt.getY()
        # All GraphicsObjects
        for mousePart in rodent:
            mousePart.move(dx, dy)
        rodentPt = p

    # Wait for a mouse click
    win.getMouse()
    win.close()

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)