#!/usr/bin/python3

""" Function to return the Pascal Triangle """


def pascal_triangle(n):
    """
    Function to return a list of lists representing
    Pascal's triangle with n rows.

    Args:
        n (int): to determine the rows
    """
    if n <= 0:
        return []

    triangle = []
    for y in range(n):
        row = [1] * (y + 1)
        if y > 1:
            for z in range(1, y):
                row[z] = triangle[y - 1][z - 1] + triangle[y - 1][z]
        triangle.append(row)

    return triangle
