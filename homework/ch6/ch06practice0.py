
def add_fruit(inventory, fruit, quantity=0):
    """
    Adds quantity of fruit to inventory.

       >>> new_inventory = {}
       >>> add_fruit(new_inventory, 'strawberries', 10)
       >>> 'strawberries' in new_inventory
       True
       >>> new_inventory['strawberries']
       10
       >>> add_fruit(new_inventory, 'strawberries', 25)
       >>> new_inventory['strawberries']
       35
     """
    if fruit in inventory:
            inventory[fruit] += quantity
    else:
            inventory [fruit] = quantity

def open_file():
    name = "Jonah"
    myfile = open('list.txt', 'w')
    myfile.write(f"Hello, this is {name} here, writing in a text file with pyhthon!")
    myfile.close()
    myfile = open('list.txt', 'r')
    contents = myfile.read()
    myfile.close()
    print(contents)

def list():
    myfile = open('list.txt', 'w')
    myfile.write("this\nthat\nstuff\nsuch")
    myfile.close()
    items = []
    open('list.txt', 'r')
    for line in myfile:
                items.append(line)
    myfile.close()

    print(items)

def list():
    myfile = open('list.txt', 'w')
    myfile.write("13\n97\n42\n17\n11")
    myfile.close()
    f = open('list.txt', 'r')
    items = f.read().splitlines()

    print(items)





if  __name__ == '__main__':
    import doctest
    doctest.testmod()
