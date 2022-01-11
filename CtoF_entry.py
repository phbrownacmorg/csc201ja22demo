from graphics import *
from typing import List

def main(args:List[str]) -> int:
    # Do nothing, graphically
    win:GraphWin = GraphWin('Click to close', 200, 200)
    win.setCoords(-1, -1, 1, 1)

    instructions:Text = Text(Point(0, .5), 'Click to convert\nto Fahrenheit')
    instructions.draw(win)

    degC_blank:Entry = Entry(Point(0, 0), 5)
    degC_blank.setFill('white')
    degC_blank.setText('0') # Default value, in case of an early click
    degC_blank.draw(win)

    degC_label:Text = Text(Point(.5, 0), '\u00b0C')
    degC_label.draw(win)

    # Label to display output
    outputLabel:Text = Text(Point(0, -0.5), '')
    outputLabel.draw(win)

    # Click to convert
    win.getMouse()

    # Get input
    degC:float = 0
    degCstring:str = degC_blank.getText()
    degC = float(degCstring)
    # Convert to output
    degF:float = degC * (9/5) + 32
    outputLabel.setText(str(round(degF, 1)) + '\u00b0 F')
    instructions.setText('Click again to exit')

    # Wait for a mouse click
    win.getMouse()
    win.close()

    # Conventional return value indicating successful completion
    return 0

if __name__ == '__main__':
    import sys
    main(sys.argv)