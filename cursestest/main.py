# coding: utf8
import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()

    a = ' '


    while a != 'q':
        for y in range(0, 5):
            for x in range(0, 5):
                stdscr.addch(y, x, 117)

        stdscr.refresh()
        a = stdscr.getkey()

curses.wrapper(main)