def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False

        return True

def num_digits(n):
    """
      >>> num_digits(12345)
      5
      >>> num_digits(0)
      1
      >>> num_digits(-12345)
      5
    """
    n = abs(n)

    if n == 0:
        return 1

    count = 0
    while n > 0:
        count += 1
        n = n // 10

    return count


def num_even_digits(n):
    """
      >>> num_even_digits(123456)
      3
      >>> num_even_digits(2468)
      4
      >>> num_even_digits(1357)
      0
      >>> num_even_digits(2)
      1
      >>> num_even_digits(20)
      2
    """
    n = abs(n)
    count = 0

    while n > 0 :
        digit = n % 10 
        if digit % 2 == 0:
            count += 1
        n = n // 10

    return count












if  __name__ == '__main__':
    import doctest
    doctest.testmod()
