# tuple is same as lists but it can be created using simple pranthises "()"
# we can't edit or delete data of tuple it means tuple is immutable

coordinates = (4,5)
# coordinates[1] = 10 #we cant do this
print(coordinates[0])

# we can also combine lists and tuples
# here also we can't chane current values but we can add new tuplles in this list and delete tuples form list
coord = [(4,5),(10,15),(20,30)]
coord.insert(1,(20,25))
print(coord)
coord.remove((20,25))
print(coord)