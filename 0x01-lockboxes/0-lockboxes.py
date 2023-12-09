#!/usr/bin/python3
"""Determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """ Method that determines if all boxes can be opened """

    for unopened_box in range(1, len(boxes)):

        open = False
        # Variable to track if the current unopened box can be opened

        for box in range(len(boxes)):
            """
            iterating over all the boxes to check if the keys in
            each box can open the current unopened box
            """
            if unopened_box in boxes[box] and box != unopened_box:
                """
                checks if the current unopened box is
                listed in the keys of the current box.
                ensures that the current box is not the
                same as the unopened box
                """
                open = True
                break
        if not open:
            return False

    return True
