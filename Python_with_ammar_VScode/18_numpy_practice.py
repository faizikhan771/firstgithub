import numpy as np
from numpy.core.fromnumeric import reshape
# Creating an array using numpy
# food = np.array(["Pakora", "Samosa", "Raita"])
# print(food)
# print(type(food))

# prices = np.array([9,9,9])
# print(prices)
# print(type(prices))
# print(len(food))
# print(len(prices))
# print(food[2])
# print(prices[2])
# print(food[0:])
# zero method to make an array
# f= np.zeros(6)
# print(f)
# # ones method
# f = np.ones(4)
# print(f)
# g = np.empty(6)
# print(g)
# h = np.arange(10)
# print(h)

# # table of 5
# s = np.arange(5,55,5)
# print(s)
# z = np.linspace(0,18, num=5)
# print(z)

# Array functions
# a = np.array([10,12,15,2,4,6,100,320,0,5,10.3])
# print(a)
# a.sort()
# print(a)
# b = np.array([10.2,33.1,33,21.2,19,400])
# print(b)
# c = np.concatenate((a,b))
# print(c)
# c.sort()
# print(c)

# 2-D arrays

# l = np.array([[1,2],[3,4]])
# print(l)
# k = np.array([[11,22],[33,44]])
# print(k)
# j = np.concatenate((l,k), axis=1)
# # to find dimension
# print("the dimension of l is:", l.ndim)
# print("the dimension of k is:", k.ndim)
# print("the dimension of j is:", j.ndim)
# print(l.size) # size mean number of elements
# print(j.size) 
# f = np.arange(10).reshape((5,2))
# print(f)
# d = np.array([1,2,3,4,5])
# e = d[2:5]
# print(e)

v = np.array([[[1,2,22],[3,4,44]],[[5,6,66],[7,8,880]]])
print(v)
print(v.size)
print(v.ndim)
print(v[1,1,2])
print(v[0,0,2])
v[0,1,2] = 890
print(v)