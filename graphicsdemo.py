from graphics import *
from typing import List

def main(args:List[str]) -> int:
    # Do nothing, graphically
    win:GraphWin = GraphWin('Graphics objects', 200, 200)

    # Pixels
    win.plotPixel(10, 10, 'blue')
    win.plot(10, 15, 'red')

    # Point
    p0:Point = Point(50, 50)
    p0.setOutline('dark green')
    p0.draw(win)

    center:Point = Point(100, 100)
    center.setOutline('maroon')
    # Wait to draw it

    # Circle
    circ:Circle = Circle(center, 40)
    circ.setFill('light blue')
    circ.draw(win)

    # Line
    line:Line = Line(p0, center)
    line.setOutline('blue')
    line.setWidth(5)
    line.setArrow('first')
    line.draw(win)

    # Rectangle
    p1:Point = Point(10, 150)
    rect:Rectangle = Rectangle(p1, center)
    rect.setFill('green')
    rect.draw(win)

    # Oval
    oval:Oval = Oval(center, p1)
    oval.setFill('gold')
    oval.draw(win)

    # Polygon
    p2:Point = Point(150, 50)
    poly:Polygon = Polygon(p0, center, p2)
    poly.setFill('bisque')
    poly.draw(win)

    # Text
    t:Text = Text(Point(100, 20), 'Click to close')
    t.setStyle('italic')
    t.draw(win)

    center.draw(win) # Last thing drawn wins

    # Wait for a mouse click
    win.getMouse()
    win.close()

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)