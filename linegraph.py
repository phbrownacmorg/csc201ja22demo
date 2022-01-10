from graphics import *
from typing import List

def main(args:List[str]) -> int:
    # Do nothing, graphically
    win:GraphWin = GraphWin('Click to close', 300, 300)

    # Data from https://scdhec.gov/sites/default/files/afs-covid/county-dashboard/Suppressed County Data by Week.csv
    dates:List[str] = ['11/6', '11/13', '11/20', '11/27', '12/4', '12/11', '12/18']
    cases:List[int] = [224, 211, 243, 211, 312, 313, 343]
    barMaxY = 350

    win.setCoords(-1, -barMaxY * .1, len(cases) * 1.1, barMaxY * 1.1)

    # Draw axes
    origin:Point = Point(0, 0)
    xAxis:Line = Line(origin, Point(len(cases) + .5, 0))
    xAxis.setArrow('last')
    xAxis.draw(win)

    yAxis:Line = Line(origin, Point(0, barMaxY * 1.05))
    yAxis.setArrow('last')
    yAxis.draw(win)

    for i in range(len(cases) - 1):
        line:Line = Line(Point(i+.5, cases[i]), Point(i+1.5, cases[i+1]))
        line.draw(win)

        dateLabel:Text = Text(Point(i + 0.5, -barMaxY * 0.05), dates[i])
        dateLabel.setSize(6)
        dateLabel.draw(win)

    dateLabel:Text = Text(Point(len(cases) - 0.5, -barMaxY * 0.05), dates[-1])
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