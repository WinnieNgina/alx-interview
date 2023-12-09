#!/usr/bin/python3
"""Determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """ Method that determines if all boxes can be opened """

    for unopened_box in range(1, len(boxes)):

        open = False
        # Variable to track if the current unopened box can be opened

        for box in range(len(boxes)):
            """
            Iterate over all the boxes to check if the keys in
            each box can open the current unopened box
            """
            if unopened_box in boxes[box] and box != unopened_box:
                """
                Checks if the current unopened box is
                listed in the keys of the current box.
                Second check prevents self-referential scenarios
                where a box has its own key.
                """
                open = True
                break
        if not open:
            return False

    return True
