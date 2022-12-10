"""
Module containing six different calculation
functions that are called upon in the controller
file and calculate the final grade percentage based upon
how many boxes in the application have been checked.
"""


def compute1(a, b):
    """
    Method to calculate the final grade
    percentage when only the first box is checked.
    :param a: The weight percentage in the first row.
    :param b: The grade percentage in the first row.
    :return: The result of the calculation.
    """
    result = (a * b) / a
    return result


def compute2(a, b, c, d):
    """
    Method to calculate the final grade
    percentage when the first and second
    boxes are checked.
    :param a: The weight percentage in the first row.
    :param b: The grade percentage in the first row.
    :param c: The weight percentage in the second row.
    :param d: The grade percentage in the second row.
    :return: The result of the calculation.
    """
    nume = (a * b) + (c * d)
    deno = a + c
    result = nume / deno
    return result


def compute3(a, b, c, d, e, f):
    """
    Method to calculate the final grade percentage
    when the first, second, and third boxes are checked.
    :param a: The weight percentage in the first row.
    :param b: The grade percentage in the first row.
    :param c: The weight percentage in the second row.
    :param d: The grade percentage in the second row.
    :param e: The weight percentage in the third row.
    :param f: The grade percentage in the third row.
    :return: The result of the calculation.
    """
    nume = (a * b) + (c * d) + (e * f)
    deno = a + c + e
    result = nume / deno
    return result


def compute4(a, b, c, d, e, f, g, h):
    """
    Method to calculate the final grade percentage
    when boxes one through four are checked.
    :param a: The weight percentage in the first row.
    :param b: The grade percentage in the first row.
    :param c: The weight percentage in the second row.
    :param d: The grade percentage in the second row.
    :param e: The weight percentage in the third row.
    :param f: The grade percentage in the third row.
    :param g: The weight percentage in the fourth row.
    :param h: The grade percentage in the fourth row.
    :return: The result of the calculation.
    """
    nume = (a * b) + (c * d) + (e * f) + (g * h)
    deno = a + c + e + g
    result = nume / deno
    return result


def compute5(a, b, c, d, e, f, g, h, i, j):
    """
    Method to calculate the final grade percentage
    when boxes one through five are checked.
    :param a: The weight percentage in the first row.
    :param b: The grade percentage in the first row.
    :param c: The weight percentage in the second row.
    :param d: The grade percentage in the second row.
    :param e: The weight percentage in the third row.
    :param f: The grade percentage in the third row.
    :param g: The weight percentage in the fourth row.
    :param h: The grade percentage in the fourth row.
    :param i: The weight percentage in the fifth row.
    :param j: The grade percentage in the fifth row.
    :return: The result of the calculation.
    """
    nume = (a * b) + (c * d) + (e * f) + (g * h) + (i * j)
    deno = a + c + e + g + i
    result = nume / deno
    return result


def compute6(a, b, c, d, e, f, g, h, i, j, k, l):
    """
    Method to calculate the final grade percentage
    when all six boxes are checked.
    :param a: The weight percentage in the first row.
    :param b: The grade percentage in the first row.
    :param c: The weight percentage in the second row.
    :param d: The grade percentage in the second row.
    :param e: The weight percentage in the third row.
    :param f: The grade percentage in the third row.
    :param g: The weight percentage in the fourth row.
    :param h: The grade percentage in the fourth row.
    :param i: The weight percentage in the fifth row.
    :param j: The grade percentage in the fifth row.
    :param k: The weight percentage in the sixth row.
    :param l: The grade percentage in the sixth row.
    :return: The result of the calculation.
    """
    nume = (a * b) + (c * d) + (e * f) + (g * h) + (i * j) + (k * l)
    deno = a + c + e + g + i + k
    result = nume / deno
    return result
