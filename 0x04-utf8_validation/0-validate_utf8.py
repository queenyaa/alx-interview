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
    # Variable to track the number of bytes left for a multi-byte character
    bytes_left = 0

    # Iterate through each byte in the data
    for byte in data:
        # If bytes_left is 0, this byte should be the start of a new character
        if bytes_left == 0:
            if byte >> 7 == 0:
                bytes_left = 0
            elif byte >> 5 == 0b110:
                bytes_left = 1
            elif byte >> 4 == 0b1110:
                bytes_left = 2
            elif byte >> 3 == 0b11110:
                bytes_left = 3
            else:
                # Invalid start of a character
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            bytes_left -= 1

            # If bytes_left is negative, there are too many continuation bytes
            if bytes_left < 0:
                return False

    # If there are leftover bytes, it means the data is incomplete
    return bytes_left == 0
