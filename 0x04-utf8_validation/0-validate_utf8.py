#!/usr/bin/python3

"""
Function to validate UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data (list): list of integers
    Returns:
        True if data is valid UTF-8 encoding
        False if data is not valid UTF-8 encoding
    """
    bytes_left = 0

    for val in data:
        byte = val & 255
        if bytes_left:
            if byte >> 6 != 2:
                return False
            bytes_left -= 1
            continue
        while (1 << abs(7 - bytes_left)) & byte:
            bytes_left += 1
        if bytes_left == 1 or bytes_left > 4:
            return False
        bytes_left = max(bytes_left - 1, 0)
    return bytes_left == 0
