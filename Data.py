import numpy as np
# #One dimensional array
# a = np.array([1, 2, 3])
# print(type(a))
# print(a.dtype)
# #rank or axis
# print(a.ndim)
# #size attribute for array length
# print(a.size)
# ##shape attribute for shape
# print(a.shape)

# #Two dimensional array
# b = np.array([[1.3, 2.4], [0.3, 4.1]])
# print(b.dtype)
# print(b.ndim)
# print(b.size)
# print(b.shape)
# #itemsize defines the size in bytes of each item in the array
# print(b.itemsize)
# #data is the buffer containing the actual elements of the array
# print(b.data)

# #Creating an array
# c = np.array([[1, 2, 3], [4, 5, 6]])
# print(c)
# d = np.array(((1, 2, 3), (4, 5, 6)))
# print(d)
# e = np.array([(1, 2, 3), [4, 5, 6], (7, 8, 9)])
# print(e)
# print(e.ndim)
# print(e.size)
# print(e.shape)

# #Types of Data
# g = np.array([['a', 'b'], ['c', 'd']])
# print(g)
# print(g.dtype.name)

# #Intrinsic Creation of an array
# #the zeros() function creates an array full of zeroes with dimensions defined by the shape argument
# print  (np.zeros((3, 3)))
# #the ones() function creates an array full of ones in a very similar way
# print (np.ones((3,3)))

# #arange() function is used for generating a range of numbers specified as arguments
# print(np.arange(10))
# print(np.arange(2, 8))
# print(np.arange(0, 6, 0.6))
# #use the reshape() function to create two dimensional arrays
# print(np.arange(0, 12).reshape(3, 4))
# #the linspace() function acts like arange but specifies the number of elements the range should be divided into, instead of the number of steps between one element and the next
# print(np.linspace(0, 10, 5))
# #the random function returns random numbers
# print(np.random.random(3))
# print(np.random.random((3, 3)))

#Basic Operations
#Arithmetic Operators
a = np.arange(4)
print(a + 4)
print(a*2)
b = np.arange(4, 8)
print (a + b)
print (a - b)
print (a * b)
print (a * np.sin(b))
print (a * np.sqrt(b))

A = np.arange(9).reshape(3, 3)
B = np.ones((3, 3))
print (A * B)

print(5 +5)
#The Matrix Product
