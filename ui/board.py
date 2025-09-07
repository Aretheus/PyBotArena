import curses
from models.math import Point2d

class BoardWidget:
    def __init__(self, pad: curses.window = None):
        self._pad = pad or curses.newpad(25, 25)

    def draw(self):
        pad = self._pad
        pad.border()
        pad.addstr(2, 1, "hello")
        pad.noutrefresh(0, 0, 1, 1, 25, 25)
