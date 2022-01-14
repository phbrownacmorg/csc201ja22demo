# Basic mouse interaction

from graphics import *
import math
from typing import List

def makeHead(r:float, color:str) -> Circle:
    head:Circle = Circle(Point(0, 0), r)
    head.setFill(color)
    head.setOutline(color)
    return head

def makeMouseEar(r:float, angle:float) -> Circle:
    earPt:Point = Point(1.3 * r * math.cos(angle),
                        1.3 * r * math.sin(angle))
    ear:Circle = Circle(earPt, r * .5)
    ear.setFill('gray')
    ear.setOutline('gray')
    return ear

def makeEye(angle:float, r:float, color:str) -> Oval:
    lowerPt:Point = Point(0, r * -0.2)
    upperPt:Point = Point(r * math.cos(angle), r * math.sin(angle))
    eye:Oval = Oval(lowerPt, upperPt)
    eye.setFill(color)
    return eye

def makeMouthPart(centerPt:Point, r:float, angle:float) -> Line:
    endPt:Point = Point(centerPt.getX() + 0.5 * r * math.cos(angle),
                        centerPt.getY() + 0.5 * r * math.sin(angle))
    mouthPart:Line = Line(centerPt, endPt)
    return mouthPart

def makeMouse() -> List[GraphicsObject]:
    radius:float = 0.05
    rodent:List[GraphicsObject] = [] # Empty list
    rodent.append(makeHead(radius, 'gray'))

    # Ears
    for i in range(2):
        angle = (math.pi/3) + i * (math.pi/3)
        rodent.append(makeMouseEar(radius, angle))

    # Eyes
    for i in range(2):
        angle:float = math.radians(50) + i * math.radians(80)
        rodent.append(makeEye(angle, radius, 'black'))

    # Mouth
    # BROKEN. The side of the mouth with i == 1 is bigger than the side with i == 0.
    for i in range(2):
        angle = math.radians(330) - i * math.radians(120)
        meeting:Point = Point(0, -0.35 * radius)
        rodent.append(makeMouthPart(meeting, radius, angle))
            
    return rodent

def makeCat() -> List[GraphicsObject]:
    radius:float = 0.2
    cat = []

    cat.append(makeHead(radius, 'orange'))

    # Eyes
    for i in range(2):
        angle:float = math.radians(50) + i * math.radians(80)
        cat.append(makeEye(angle, radius, 'green'))

    # Mouth
    # BROKEN. The side of the mouth with i == 1 is bigger than the side with i == 0.
    for i in range(2):
        angle = math.radians(330) - i * math.radians(120)
        meeting:Point = Point(0, -0.35 * radius)
        cat.append(makeMouthPart(meeting, radius, angle))

    return cat

def getLocation(animal:List[GraphicsObject]) -> Point:
    return animal[0].getCenter()

def moveTo(dest:Point, animal:List[GraphicsObject]) -> None:
    # Center of the head, which is item 0 on the list
    currentPos:Point = getLocation(animal)
    dx:float = dest.getX() - currentPos.getX()
    dy:float = dest.getY() - currentPos.getY()
    # Everything's a GraphicsObject, even though they're not all the same
    for part in animal:
        part.move(dx, dy)

def drawAnimal(win:GraphWin, animal:List[GraphicsObject]) -> None:
    for part in animal:
        part.draw(win)

def main(args:List[str]) -> int:
    # Do nothing, graphically
    win:GraphWin = GraphWin('Click to close', 300, 300)
    win.setCoords(-1, -1, 1, 1)

    # Create a "mouse" to chase the mouse clicks
    mouse:List[GraphicsObject] = makeMouse()
    cat:List[GraphicsObject] = makeCat()

    # Initially off the screen
    moveTo(Point(2, 0), mouse)
    moveTo(Point(4, 0), cat)

    drawAnimal(win, mouse)
    drawAnimal(win, cat)
    
    # Collect mouse clicks
    for i in range(5):
        p = win.getMouse()
        moveTo(getLocation(mouse), cat)
        moveTo(p, mouse)

    # Wait for a mouse click
    win.getMouse()
    win.close()

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)