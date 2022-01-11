from graphics import *
from typing import List

def main(args:List[str]) -> int:
    # Do nothing, graphically
    win:GraphWin = GraphWin('Click to close', 200, 200)
    win.setCoords(-1, -1, 1, 1)

    instructions:Text = Text(Point(0, .75), 'Click to set box color')
    instructions.draw(win)

    rLabel:Text = Text(Point(-.9, .25), 'R:')
    rLabel.draw(win)
    rEntry:Entry = Entry(Point(-.6, .25), 3)
    rEntry.setFill('white')
    rEntry.setText('0')
    rEntry.draw(win)

    gLabel:Text = Text(Point(-.2, .25), 'G:')
    gLabel.draw(win)
    gEntry:Entry = Entry(Point(.1, .25), 3)
    gEntry.setFill('white')
    gEntry.setText('0')
    gEntry.draw(win)

    bLabel:Text = Text(Point(.5, .25), 'B:')
    bLabel.draw(win)
    bEntry:Entry = Entry(Point(.8, .25), 3)
    bEntry.setFill('white')
    bEntry.setText('0')
    bEntry.draw(win)

    # Box to color
    box:Rectangle = Rectangle(Point(-.9, -.2), Point(.9, -.9))
    box.setFill('white')
    box.draw(win)

    win.getMouse()
    # Set the box color
    box.setFill(color_rgb(int(rEntry.getText()), int(gEntry.getText()), 
                int(bEntry.getText())))
    instructions.setText('Click again to exit')

    # Wait for a mouse click
    win.getMouse()
    win.close()

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)