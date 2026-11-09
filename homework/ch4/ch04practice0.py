prefixes = "JKLMNOPQ"
suffix = "ack"

    

for letter in prefixes:
    if letter == "Q" or letter == "O":
        letter += "u"
    
    print(letter + suffix)
















if  __name__ == '__main__':
    import doctest
    doctest.testmod()
