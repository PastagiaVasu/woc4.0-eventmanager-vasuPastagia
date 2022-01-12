# im using numpy for pyscript 1
import numpy as np

# (1). Conversion from other Python structures (i.e. lists and tuples)
# listArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(listArray)
# print(listArray.shape)
# print(listArray.size)

# (2). Intrinsic NumPy array creation functions (e.g. arange, ones, zeros, etc.)
zerosAr = np.zeros((2, 3))
# np.zeros will create array with value (0) of mentioned size
# print(zerosAr)
# print(zerosAr.dtype)

range = np.arange(15)
# this will create an array of 15 and will contain data till 15
# print(range)
# print(range.size)
# print(range.dtype)

lspace = np.linspace(1, 50, 10)
# this linespace will create an array with equaily divide number into given number
# here it will take number between 1 to 50 and make 10 equal parts
# print(lspace)

emt = np.empty((2, 2))
# this empty func will create an array of empty value which means it contains only grabage values or some memeory address
# print(emt)

emt_like = np.empty_like(lspace)
# this func will create an array of same size lsapce has but this new array contain grabage value or memeory address
# print(emt_like)

identity = np.identity(10)
# this identity func will create identity matrix of given size
# print(identity)
# print(identity.shape)
# print(identity.size)

# this reshape func will reshape my given array into given size
# i have made one array from 0 - 98
arr = np.arange(99)
print(arr)
# now im reshaping my arr to 3 * 3 2d array
arr = arr.reshape(3, 33)
print(arr)

# new i want to make my array as original array then i can use ravel() func
arr = arr.ravel()
print("new this array becomes original array : ")
print(arr)