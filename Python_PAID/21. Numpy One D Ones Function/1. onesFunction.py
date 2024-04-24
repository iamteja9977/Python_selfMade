# 1D Array using ones Function Numpy
from numpy import *
a = ones(5)
#a = ones(5, dtype=int)

print("**** Accessing Individual Elements ****")
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print()

print("**** Accessing by For Loop ****")
for el in a:
	print(el)
print()

print("**** Accessing by For Loop with Index ****")	
n = len(a)
for i in range(n):
	print('index',i,'=',a[i])
print()

print("**** Accessing by While Loop ****")	
n = len(a)
i = 0
while i < n:
	print('index',i,'=',a[i])
	i+=1