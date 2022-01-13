# defining function
from math import *


def sayhi(name,age):
    print("Hello " + name + "..!")
    print("Age :=" + str(age))

# returning data from func
def cube(n1):
    return n1*n1*n1

sayhi("Vasu",20)
sayhi("Jay",21)

sqrt = cube(2)
print("Cube of 2 = "+str(sqrt))