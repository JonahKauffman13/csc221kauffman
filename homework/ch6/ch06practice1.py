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














if  __name__ == '__main__':
    import doctest
    doctest.testmod()
