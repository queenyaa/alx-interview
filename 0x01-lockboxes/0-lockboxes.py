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
    keys = set([0])
    opened = set()

    while keys:
        key = keys.pop()
        opened.add(key)
        for box in boxes[key]:
            if box not in opened:
                keys.add(box)

    return len(opened) == len(boxes)
