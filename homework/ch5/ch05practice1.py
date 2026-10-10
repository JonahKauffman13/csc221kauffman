def compare(a, b):
    """
      >>> compare(8, 4)
      1
      >>> compare(7, 7)
      0
      >>> compare(2, 9)
      -1
      >>> compare(42, 1)
      1
      >>> compare('c', 'a')
      1
      >>> compare('p', 'p')
      0
    """

    if a > b:
        return 1
    if a == b:
        return 0
    if a < b:
        return -1

import math
def hypotenuse(a, b):
    """
      >>> hypotenuse(3, 4)
      5.0
      >>> hypotenuse(12, 5)
      13.0
      >>> hypotenuse(7, 24)
      25.0
      >>> hypotenuse(9, 12)
      15.0
    """

    r = a ** 2 + b ** 2
    return math.sqrt(r)


def slope(x1, y1, x2, y2):
    """
      >>> slope(5, 3, 4, 2)
      1.0
      >>> slope(1, 2, 3, 2)
      0.0
      >>> slope(1, 2, 3, 3)
      0.5
      >>> slope(2, 4, 1, 2)
      2.0
    """
    return (y2 - y1) / (x2 - x1)

def intercept(x1, y1, x2, y2):
    """
      >>> intercept(1, 6, 3, 12)
      3.0
      >>> intercept(6, 1, 1, 6)
      7.0
      >>> intercept(4, 6, 12, 8)
      5.0
    """
    m = slope(x1,y1, x2, y2)
    return y1 - m * x1


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 == 0
    return not is_even(n)

def is_factor(f, n):
    """
      >>> is_factor(3, 12)
      True
      >>> is_factor(5, 12)
      False
      >>> is_factor(7, 14)
      True
      >>> is_factor(2, 14)
      True
      >>> is_factor(7, 15)
      False
    """
    return n % f == 0 


def is_multiple(m, n):
    """
      >>> is_multiple(12, 3)
      True
      >>> is_multiple(12, 4)
      True
      >>> is_multiple(12, 5)
      False
      >>> is_multiple(12, 6)
      True
      >>> is_multiple(12, 7)
      False
    """
    return is_factor(n, m)


def f2c(t):
    """
      >>> f2c(212)
      100
      >>> f2c(32)
      0
      >>> f2c(-40)
      -40
      >>> f2c(36)
      2
      >>> f2c(37)
      3
      >>> f2c(38)
      3
      >>> f2c(39)
      4
    """
    return round((t-32) * 5/9)


def c2f(t):
    """
      >>> c2f(0)
      32
      >>> c2f(100)
      212
      >>> c2f(-40)
      -40
      >>> c2f(12)
      54
      >>> c2f(18)
      64
      >>> c2f(-48)
      -54
    """
    return round(t * 9 / 5 +32)



if  __name__ == '__main__':
    import doctest
    doctest.testmod()
