"""
Create by Killer at 2019-05-23 14:11
"""
import numpy as np

# Create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])

# Print the ndarray just created
print()
print("x = ", x)
print()

# Print information about x
print('x has dimensions: ', x.shape)
print('x is an object of type: ', type(x))
print('The elements in x are of type: ', x.dtype)

y = np.array(["Hello", "Just", "Spiders"])

# Print the ndarray just created
print()
print("y = ", y)
print()

# Print information about x
print('y has dimensions: ', y.shape)
print('y is an object of type: ', type(y))
print('The elements in y are of type: ', y.dtype)

z = np.array([1, 2, 'Helo'])

# Print the ndarray just created
print()
print("z = ", z)
print()

# Print information about x
print('z has dimensions: ', z.shape)
print('z is an object of type: ', type(z))
print('The elements in z are of type: ', z.dtype)

