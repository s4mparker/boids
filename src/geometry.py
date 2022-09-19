import math, random, functools
from math import sin, cos, atan2

# Packaging
__all__ = ['Vector2D', 'Point2D']

class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector2D ({self.x}, {self.y}, {self.angle})'

    # --- Operators ----------------------------------------------------------

    def __add__(self, operand):
        if type(operand) is Point2D:
            raise TypeError('vector + point is an invalid operation')
        elif type(operand) is Vector2D:
            return Vector2D(self.x + operand.x, self.y + operand.y)
        elif type(operand) in [int, float]:
            return Vector2D(self.x + operand, self.y + operand)
        else:
            raise TypeError('unexpected operand')

    def __sub__(self, operand):
        if type(operand) is Point2D:
            raise TypeError('vector - point is an invalid operation')
        elif type(operand) is Vector2D:
            return Vector2D(self.x - operand.x, self.y - operand.y)
        elif type(operand) in [int, float]:
            return Vector2D(self.x - operand, self.y - operand)
        else:
            raise TypeError('unexpected operand')

    def __mul__(self, operand):
        if type(operand) is Vector2D:
            return self.x * operand.x + self.y * operand.y
        elif type(operand) in [int, float]:
            return Vector2D(self.x * operand, self.y * operand)
        else:
            raise TypeError('unexpected operand')

    def __truediv__(self, operand):
        if type(operand) in [int, float]:
            if operand == 0:
                raise ZeroDivisionError('cannot divide by 0')
            else:
                return Vector2D(self.x / operand, self.y / operand)
        else:
            raise TypeError('unexpected operand')

    def __xor__(self, operand):
        if type(operand) is Vector2D:
            return math.atan2(
                operand.x * self.y - operand.y * self.x, 
                operand.x * self.x + operand.y * self.y
            ) * 180 / math.pi
        else:
            raise TypeError('unexpected operand')

    def __and__(self, operand):
        if type(operand) in [int, float]:
            r = -operand * math.pi / 180
            print(r)
            return Vector2D(
                cos(r) * self.x - sin(r) * self.y,
                sin(r) * self.x + cos(r) * self.y
            )
        else:
            raise TypeError('unexpected operand')

    # --- Properties ---------------------------------------------------------

    @property
    def angle(self):
        return Vector2D(0, 1) ^ self

    @property
    def magnitude(self):
        if self.x == 0 and self.y == 0:
            return 0
        else:
            return math.sqrt(self.x**2 + self.y**2)

    @property
    def unit(self):
        m = self.magnitude
        if m == 0 : return Vector2D(0, 0)
        else: return Vector2D(self.x / m, self.y / m)

    # --- Class Methods ------------------------------------------------------

    @classmethod
    def random(cls, d1, d2):
        return cls(random.randint(0, d1), random.randint(0, d2))

class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point2D ({self.x}, {self.y})'

    # --- Operators ----------------------------------------------------------

    def __add__(self, operand):
        if type(operand) is Point2D:
            raise TypeError('point + point is an invalid operation')
        elif type(operand) is Vector2D:
            return Point2D(self.x + operand.x, self.y + operand.y)
        else:
            raise TypeError('unexpected operand')

    def __sub__(self, operand):
        if type(operand) is Point2D:
            return Vector2D(self.x - operand.x, self.y - operand.y)
        elif type(operand) is Vector2D:
            return Point2D(self.x - operand.x, self.y - operand.y)
        else:
            raise TypeError('unexpected operand')

    # --- Class Methods ------------------------------------------------------

    @classmethod
    def random(cls, d1, d2):
        return cls(random.randint(0, d1), random.randint(0, d2))
        
if False and __name__ == '__main__':
    p1 = Point2D(1, 1)
    print(p1)

    p2 = Point2D(2, 2)
    print(p2)

    v1 = p2 - p1
    print(v1)

    p3 = p2 - v1
    print(p3)

    p4 = p1 + v1
    print(p4)

    v2 = Vector2D(2, 2) + v1
    print(v2)

    v3 = Vector2D(4, 4) - v1
    print(v3)

    v4 = Vector2D(1, 2) + Vector2D(2, 1)
    print(v4)

    v5 = v4 - Vector2D(5, 5)
    print(v5)

    u1 = Vector2D(10, 0).unit
    print(u1)
    print(u1.magnitude)

    v6 = Vector2D(0, 1)
    v7 = Vector2D(1, 1)
    print(v6 @ v7)

if __name__ == '__main__':
    p1 = Point2D(0, 0)
    p2 = Point2D(1, 1)
    print(p1 - p2)

