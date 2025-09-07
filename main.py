import curses
from ui.board import BoardWidget

def main(stdscr: curses.window):
    board = BoardWidget()

    stdscr.clear()
    stdscr.noutrefresh()

    board.draw()

    curses.doupdate()
    stdscr.getkey()

if __name__ == '__main__':
    curses.wrapper(main)
