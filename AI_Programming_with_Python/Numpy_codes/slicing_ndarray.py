"""
Create by Killer at 2019-05-23 15:06
"""
import numpy as np

"""
1: ndarray[start:end]
2: ndarray[start:]
3. ndarray[:end]
"""

# Create a 4x5 ndarray that contains integers from 0 to 19
x = np.arange(20).reshape(4, 5)

print()
print('x = \n', x)
print()

# select all the elements that are in the 2nd through 4th rows and in the 3rd to 5th columns
z = x[1:4, 2:5]
print('z = \n', z)

# select the same elements as above using method 2
w = x[1:, 2:5]
print('w = \n', w)

# select all the elements in the 3rd row
v = x[2, :]

print()
print('v = \n', v)

# select all the elements in 3rd column
q = x[:, 2]
print()
print('q = ', q)

# select all the elements in the 3rd column but return a rand 2 ndarray
R = x[:, 2:3]
print()
print('R = \n', R)

# the slice of the original array x is not copied in the variable z.
# that means that if make changes in z will be in effect changing the
# elements in x as well.
z[2,2] = 555
print()
print("Modified z = \n", z)
print()
print("After modified x = \n", x)

# If want to create a new ndarray that cotains a copy of the values in the slice we need to use the np.copy function.
# by using the copy command,we are creating new ndarrays that are completely independent of each other.
Z = np.copy(x[1:4, 2:5])

W = x[1:4, 2:5].copy()

Z[2, 2] = 444
W[2, 2] = 666

print()
print("x = \n", x)
print()
print("Z = \n", Z)
print()
print("W = \n", W)
