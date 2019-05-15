"""
Create by Killer at 2019-04-24 15:19
"""

from math import sqrt, acos, pi
from decimal import Decimal, getcontext

dot_num = 30

getcontext().prec = dot_num

class Vector(object):

    CANNOT_NORMALIZED_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'No unique parallel component'
    NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = 'No unique orthogonal component'
    ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = 'Only defined in two and three dimision'

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

    # 向量在基向量上的投影
    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)
        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e

    def component_parallel_to(self, basis):
        try:
            u = basis.normalized()
            weight = self.dot(u)
            return u.times_scalar(weight)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZED_ZERO_VECTOR_MSG:
                raise Exception(self.CANNOT_NORMALIZED_ZERO_VECTOR_MSG)
            else:
                raise e

    # 向量积 - 输出向量
    def area_of_triangle_with(self, v): # 两个向量 三角形面积
        return Decimal(self.area_of_parallelogram_with(v)) / Decimal('2.0')

    def area_of_parallelogram_with(self, v): # 两个向量 矩形面积
        cross_product = self.cross(v)
        return cross_product.magnitude()

    def cross(self, v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates = [ y_1*z_2 - y_2*z_1,
                                -(x_1*z_2 - x_2*z_1),
                                x_1*y_2 - x_2*y_1]
            return Vector(new_coordinates)
        except ValueError as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0', ))
                v_embedded_in_R3 = Vector(v.coordinates + ('0', ))
                return self_embedded_in_R3.cross(v_embedded_in_R3)
            elif (msg == 'too many values to unpack' or msg == 'need more than 1 value to unpack'):
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e


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

    ## Test dot & angle_with
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


    ## Test parallel & orthogonal
    # print("First pair...")
    # v = Vector(['-7.579', '-7.88'])
    # w = Vector(['22.737', '23.64'])
    # print("is parallel:", v.is_parallel_to(w))
    # print("is orthogonal:", v.is_orthogonal_to(w))
    #
    # print("Second pair...")
    # v = Vector(['-2.029', '9.97', '4.172'])
    # w = Vector(['-9.231', '-6.639', '-7.245'])
    # print("is parallel:", v.is_parallel_to(w))
    # print("is orthogonal:", v.is_orthogonal_to(w))
    #
    # print("Third pair...")
    # v = Vector(['-2.328', '-7.284', '-1.214'])
    # w = Vector(['-1.821', '1.072', '-2.94'])
    # print("is parallel:", v.is_parallel_to(w))
    # print("is orthogonal:", v.is_orthogonal_to(w))
    #
    # print("Fourth pair...")
    # v = Vector(['2.118', '4.827'])
    # w = Vector(['0', '0'])
    # print("is parallel:", v.is_parallel_to(w))
    # print("is orthogonal:", v.is_orthogonal_to(w))

    ## Test projection
    # print("#1")
    # v = Vector([3.039, 1.879])
    # w = Vector([0.825, 2.036])
    # print(v.component_parallel_to(w))
    #
    # print('\n#2')
    # v = Vector([-9.88, -3.264, -8.159])
    # w = Vector([-2.155, -9.353, -9.473])
    # print(v.component_orthogonal_to(w))
    #
    # print('\n#3')
    # v = Vector([3.009, -6.172, 3.692, -2.51])
    # w = Vector([6.404, -9.144, 2.759, 8.718])
    # vpar = v.component_parallel_to(w)
    # vort = v.component_orthogonal_to(w)
    # print("parallel component: ", vpar)
    # print("orthogonal component: ", vort)


    ##Test cross
    v = Vector(['8.462', '7.893', '-8.187'])
    w = Vector(['6.984', '-5.975', '4.778'])
    print('#1: ', v.cross(w))

    v = Vector(['-8.987', '-9.838', '5.031'])
    w = Vector(['-4.268', '-1.861', '-8.866'])
    print('#2: ', v.area_of_parallelogram_with(w))

    v = Vector(['1.5', '9.547', '3.691'])
    w = Vector(['-6.007', '0.124', '5.772'])
    print('#3: ', v.area_of_triangle_with(w))

