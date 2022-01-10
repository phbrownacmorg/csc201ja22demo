from graphics import *
from typing import List

# This works, but it's a lot of work and it's fragile.

def main(args:List[str]) -> int:
    # Do nothing, graphically
    win:GraphWin = GraphWin('Click to close', 300, 300)

    # Data from https://scdhec.gov/sites/default/files/afs-covid/county-dashboard/Suppressed County Data by Week.csv
    dates:List[str] = ['11/6', '11/13', '11/20', '11/27', '12/4', '12/11', '12/18']
    cases:List[int] = [224, 211, 243, 211, 312, 313, 343]
    barMaxY = 350

    # Draw axes
    origin:Point = Point(30, 270)
    xAxis:Line = Line(origin, Point(270, origin.getY()))
    xAxis.setArrow('last')
    xAxis.draw(win)

    yAxis:Line = Line(origin, Point(origin.getX(), 30))
    yAxis.setArrow('last')
    yAxis.draw(win)

    barWidth:int = 30
    barMaxHeight:int = 200

    for i in range(len(cases)):
        barLeft:int = origin.getX() + barWidth * i
        barRight:int = barLeft + barWidth
        barCenterX:float = (barLeft + barRight) / 2
        barTop:float = origin.getY() - barMaxHeight * (cases[i] / barMaxY)
        bar:Rectangle = Rectangle(Point(barLeft, origin.getY()),
                                    Point(barRight, barTop))
        bar.setFill('cyan')
        bar.draw(win)

        dateLabel:Text = Text(Point(barCenterX, 285), dates[i])
        dateLabel.setSize(6)
        dateLabel.draw(win)

    # Wait for a mouse click
    win.getMouse()
    win.close()

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)