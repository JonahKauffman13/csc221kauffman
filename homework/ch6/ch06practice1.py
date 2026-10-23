thing1 = {'hey': 'hola', 'yes': 'si', 'bye': 'adios'}
thing2 = {'hey', 'hello', 'bye'}
"""
  >>> type(thing1)
  <class 'dict'>
  >>> type(thing2)
  <class 'set'>
"""

d = {'2+1': '3','2+2': '4','2+3': '5'}
"""
  >>> 4 in d
  True
  >>> 'name' in d
  False
  >>> d['name'] = 'Eric'
  >>> 'name' in d
  True
"""


def counts():
    """
    >>> counts()
    >>> Please enter a string: THis String Has Upper and Lower case letters.

      a 3
      c 1
      d 1
      e 5
      g 1
      h 2
      i 2
      l 2
      n 2
      o 1
      p 2
      r 4
      s 5
      t 4
      u 1
      w 1
    """
    string = input("Please enter a string:").lower()
    counts = {}
    for char in string:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    for char in sorted(counts):
        print(char, counts[char])
    counts()




if __name__ == '__main__':
    import doctest
    doctest.testmod()
