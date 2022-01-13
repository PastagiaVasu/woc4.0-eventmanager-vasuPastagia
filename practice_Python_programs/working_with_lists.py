friends = ["Miraj","Pranav","Ayush"]
print(friends)
print(friends[-3])
# in python you can use -ve index to print data or element here -1 = 2 in above example
print(friends[1:])
# this print statement display element from 1 to till end of the list
cars = ["Audi","BMW","Skoda","Ford","Suzuki"]
print(cars[1:3])
# this will disply element from 1 to 3 but i will not incdlue 3rd element
cars[1] = "KIA"
print(cars[1])

# Function of Lists

luckey_numbers = [4,8,15,42,23,16]
names = ["Miraj","Pranav","Ayush","Jay","Dhruvi","Suru","Riddhi"]

print(names)
# Extend is same as append one list to another
# names.extend(luckey_numbers)
# print(names)
# or we can use append also
names.append("Vasu")
print(names)

# to insert element at specific position
names.insert(2,"Jay")
print(names)

# to remove element from list
# names.remove("Ayush")
# print(names)

# to clear whole list
# names.clear()
# print(names)

# we can use pop() for removing last element from list
names.pop()
print(names)

# to check whether this list contain this element or not we could use index()
print(names.index("Suru"))

# how name times this name appears in this list, we could use count func
print(names.count("Jay"))

# sort list in acending order
names.sort()
luckey_numbers.sort()
print(names)
print(luckey_numbers)

# Reverse the list
luckey_numbers.reverse()
print(luckey_numbers)

# to copy one list to another we use copy func
names2 = names.copy()
print(names2)