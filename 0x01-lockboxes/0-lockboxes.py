#!/usr/bin/python3

"""
Function that checks whether all boxes in a
list of lists can be opened
"""


def canUnlockAll(boxes):
    """Function to check list of lists

    Args:
        boxes (list of lists): contain keys used to unlock other lists
    """
    nextbox = set()

    for id_box, box in enumerate(boxes):
        if len(box) == 0 or id_box == 0:
            nextbox.add(id_box)
        for key in box:
            if key < len(boxes) and key != id_box:
                nextbox.add(key)
        if len(nextbox) == len(boxes):
            return True
    return False
