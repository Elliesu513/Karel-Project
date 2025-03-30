"""
File: PotholeFilling.py
Name: Ellie
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:Karel is at the upper left of the pothole, facing East
    """
    for i in range(3):
        move()
        turn_right()
        move()
        put_beeper()
        turn_around()
        move()
        turn_right()
        move()


def turn_around():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
