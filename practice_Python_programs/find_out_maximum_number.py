
def maxmimum(n1,n2,n3):
    if n1 >= n2 and n1 >= n3:
        print(str(n1) + " is maximum among all numbers")
    elif n2 >= n1 and n2 >= n3:
        print(str(n2) + " is maximum among all numbers")
    else:
        print(str(n3) + " is maximum among all numbers")

maxmimum(5,7,6)