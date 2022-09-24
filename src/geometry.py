import math, random
from math import sin, cos, atan2

# Packaging
__all__ = ['Vector2D', 'Point2D']

class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector2D ({self.x}, {self.y}, {self.angle})'

    def __bool__(self):
        return self.magnitude != 0

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

    # --- Properties ---------------------------------------------------------

    @property
    def angle(self):
        return self.get_angle_between_vectors(Vector2D(0, 1), self)

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

    # --- Static Methods -----------------------------------------------------

    @staticmethod
    def rotate_vector(vector, angle):
        r = -angle * math.pi / 180
        return Vector2D(
            cos(r) * vector.x - sin(r) * vector.y,
            sin(r) * vector.x + cos(r) * vector.y
        )

    @staticmethod
    def get_angle_between_vectors(vector1, vector2):
        if type(vector1) is Vector2D and type(vector2) is Vector2D:
            return math.atan2(
                vector2.x * vector1.y - vector2.y * vector1.x, 
                vector2.x * vector1.x + vector2.y * vector1.y
            ) * 180 / math.pi
        else:
            raise TypeError('unexpected operand')

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

    # --- Static Methods -----------------------------------------------------

    @staticmethod
    def get_average_point(*points):
        if any([type(point) is not Point2D for point in points]):
            raise TypeError('unexpected operand')
        else:
            avg_x, avg_y = 0, 0
            for point in points:
                avg_x += point.x
                avg_y += point.y
            return Point2D(avg_x / len(points), avg_y / len(points))

if __name__ == '__main__':
    p1 = Point2D(0, 0)
    p2 = Point2D(1, 1)
    print(p1 - p2)

