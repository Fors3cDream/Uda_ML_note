"""
Create by Killer at 2019-05-23 14:29
"""
import numpy as np

x  = np.array([1, 2, 3, 4, 5])

print()
print('x = ', x)
print()

# Let's access some elements with positive indices
print("Access element with positive indices!")
print("This is First Element in x:", x[0])
print("This is Second Element in x:", x[1])
print("This is Fifth(Last) Element in x:", x[len(x)-1])
print()

# Let's access the same elements with negative indices
print("Access element with negative indices!")
print('This is First Element in x:', x[-len(x)])
print('This is Second Element in x:', x[-len(x) + 1])
print('This is Fifth(Last) Element in x:', x[-1])

y = x.copy()
print()
print('Original y = ', y)
print()

y[3] = 20
print('Modified:\n y = ', y)
print('x = ', x)
print()

# Create a 3x3 rank 2 ndarray that contains integers from 1 to 9
z = np.array([[1,2,3], [4,5,6], [7,8,9]])

print()
print("z = \n", z)
print()

# Access some elements in z
print('This is (0, 0) Element in z: ', z[0,0])
print('This is (0, 1) Element in z: ', z[0,1])
print('This is (2, 2) Element in z: ', z[2, 2])

"""
can add and delete elements from ndarrays. using np.delete(ndarray, elements, axis) function.
This function deletes the given list of elements from the given ndarray along the spedified axis.
For rank 1 ndarrays the axis keyword is not required.For rank 2 ndarrays, axis=0 is used to select rows,
and axis=1 is used to select columns.
"""
new_x = np.array([1, 2, 3, 4, 5])
new_y = np.array([[1,2,3], [4,5,6], [7,8,9]])

print()
print("Original new x = ", x)

x = np.delete(x, [0, 4])
print()
print("Modified x = ", x)

print()
print("Original new y = ", y)

# delete the first row of y
w = np.delete(new_y, 0, axis=0)

# delete the first and last column of new y
v = np.delete(new_y, [0, 2], axis=1)

print()
print('w = ', w)

print()
print('v = ', v)

'''
We can append values to ndarrays using the np.append(ndarray, elements, axis) function.
This function appends the given list of elements to ndarray along the specified axis.
'''
x = np.array([1, 2, 3, 4, 5])
y = np.array([[1,2,3], [4,5,6], [7,8,9]])

print()
print('Original x = ', x)

x = np.append(x, 6)

print()
print('Appended x = ', x)

print()
print('Original y = \n', y)

v = np.append(y, [[7,8,9]], axis=0)
print()
print('v = \n', v)

z = np.append(y, [[9], [10], [1]], axis=1)
print()
print('z = \n', z)

"""
Insert values to ndarrays using the np.insert(ndarray, index, elements, axis) function.
This function inserts the given list of elements to ndarray right before the given index
along the spedified axis.
"""
x = np.array([1, 2, 5, 6, 7])

y = np.array([[1,2,3], [7,8,9]])

print()
print('Original x = ', x)

print()
print('Original y = \n', y)

# insert a row between the first and last row of y
w = np.insert(y, 1, [4, 5, 6], axis=0)

v = np.insert(y, 1, 5, axis=1)

print()
print('w = \n', w)
print()
print('v = \n', v)


'''
stack to ndarrays on top of each other,or to stack them side by side.The stacking is done using either the np.vstack() function
for vertical stacking, or the np.hstack() function for horizontal stacking.It is important to note that in order to stack ndarrays,
the shape of the ndarrays must match.
'''
x = np.array([1, 2])

y = np.array([[3,4], [5,6]])

print()
print('x = ', x)

print()
print('y = \n', y)

# Stack x on top of y
z = np.vstack((x, y))

# Stack x on the right of y.we need to reshape x in order to stack it on the right of y.
w = np.hstack((y, x.reshape(2, 1)))

print()
print('z = \n', z)

print()
print('w = \n', w)