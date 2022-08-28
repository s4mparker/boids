import math, random

# Packaging
__all__ = ['Vector2D', 'Point2D']

class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector2D ({self.x}, {self.y}, {self.bearing})'

    @property
    def bearing(self):
        return math.atan2(self.x, self.y) * 180 / math.pi + 180

    @property
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    @property
    def unit(self):
        m = self.magnitude
        if m == 0 : return Vector2D(0, 0)
        else: return Vector2D(self.x / m, self.y / m)

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
            return math.acos((self.x * operand.x + self.y * operand.y) / (self.magnitude * operand.magnitude)) * 180 / math.pi
        elif type(operand) in [int, float]:
            return Vector2D(self.x * operand, self.y * operand)
        else:
            raise TypeError('unexpected operand')

    def __truediv__(self, operand):
        if type(operand) in [int, float]:
            if operand == 0:
                raise ZeroDivisionError('cannot divide by 0')
            return Vector2D(self.x / operand, self.y / operand)
        else:
            raise TypeError('unexpected operand')

    @classmethod
    def random(cls, w, h):
        return cls(random.randint(0, w) - w / 2, random.randint(0, h) - h / 2)

    @classmethod
    def interpolate(cls, vectors, weights=None):
        if weights is None:
            weights = [[1 / len(vectors)] * len(vectors)]
        
        x = 0
        y = 0
        for (vector, weight) in zip(vectors, weights):
            x += vector.x * weight
            y += vector.y * weight
        
        return Vector2D(x, y)

class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point2D ({self.x}, {self.y})'

    def __add__(self, operand):
        if type(operand) is Point2D:
            raise TypeError('point + point is an invalid operation')
        elif type(operand) is Vector2D:
            return Point2D(self.x + operand.x, self.y + operand.y)
        else:
            raise TypeError('unexpected operand')

    def __sub__(self, operand):
        if type(operand) is Point2D:
            return Vector2D(operand.x - self.x, operand.y - self.y)
        elif type(operand) is Vector2D:
            return Point2D(self.x - operand.x, self.y - operand.y)
        else:
            raise TypeError('unexpected operand')

    @classmethod
    def random(cls, w, h):
        return cls(random.randint(0, w), random.randint(0, h))
        
if __name__ == '__main__':
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


