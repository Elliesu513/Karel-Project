"""
File: StepUp.py
Name: Ellie
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *


def main():
    pass
    """
    pre-condition:Karel is at 1-1, facing East
    post-condition:Karel is at 5-2, facing East
    """
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    put_beeper()
    move()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
