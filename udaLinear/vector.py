"""
Create by Killer at 2019-04-24 15:19
"""

from math import sqrt, acos, pi
from decimal import Decimal, getcontext

dot_num = 30

getcontext().prec = dot_num

class Vector(object):

    CANNOT_NORMALIZED_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError("The coordinates must be nonempty")
        except TypeError:
            raise TypeError("The coordinates must be an iterable")

    # 向量大小
    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    # 向量标准化
    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    # 向量加法
    def plus(self, v):
        new_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    # 向量减法
    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    # 向量与常量相乘 - 标量
    def times_scalar(self, c):
        new_coordinates = [ Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)

    # 向量正交
    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    # 向量平行
    def is_parallel_to(self, v):
        return (self.is_zero() or v.is_zero() or self.angle_with(v) == 0 or self.angle_with(v) == pi)

    # 是否为零向量
    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    # 向量内积
    def dot(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    # 向量夹角
    def angle_with(self, v, in_degress=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            try:
                angle_with_radians = acos(u1.dot(u2))
            except ValueError:
                theta_num = round(u1.dot(u2), dot_num//2)
                angle_with_radians = acos(theta_num)

            if in_degress:
                degress_per_radian = 180./pi
                return angle_with_radians * degress_per_radian
            else:
                return angle_with_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZED_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    # 重载 等于 运算符
    def __eq__(self, v):
        return self.coordinates == v.coordinates


if __name__ == "__main__":

    # v = Vector(['7.887', '4.138'])
    # w = Vector(['-8.802', '6.776'])
    # print(v.dot(w))
    #
    # v = Vector(['-5.955', '-4.904', '-1.874'])
    # w = Vector(['-4.496', '-8.755', '7.103'])
    # print(v.dot(w))
    #
    # v = Vector(['3.183', '-7.627'])
    # w = Vector(['-2.668', '5.319'])
    # print(v.angle_with(w))
    #
    # v = Vector(['7.35', '0.221', '5.188'])
    # w = Vector(['2.751', '8.259', '3.985'])
    # print(v.angle_with(w, in_degress=True))

    print("First pair...")
    v = Vector(['-7.579', '-7.88'])
    w = Vector(['22.737', '23.64'])
    print("is parallel:", v.is_parallel_to(w))
    print("is orthogonal:", v.is_orthogonal_to(w))

    print("Second pair...")
    v = Vector(['-2.029', '9.97', '4.172'])
    w = Vector(['-9.231', '-6.639', '-7.245'])
    print("is parallel:", v.is_parallel_to(w))
    print("is orthogonal:", v.is_orthogonal_to(w))

    print("Third pair...")
    v = Vector(['-2.328', '-7.284', '-1.214'])
    w = Vector(['-1.821', '1.072', '-2.94'])
    print("is parallel:", v.is_parallel_to(w))
    print("is orthogonal:", v.is_orthogonal_to(w))

    print("Fourth pair...")
    v = Vector(['2.118', '4.827'])
    w = Vector(['0', '0'])
    print("is parallel:", v.is_parallel_to(w))
    print("is orthogonal:", v.is_orthogonal_to(w))

