class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, other):
        return Point(self.x + other.x, self.x + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.x - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.x * other.y)

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'


p1 = Point(5, 5)
p2 = Point(4, 3)
p3 = Point(1, 2)
p4 = Point(-3, -5)

print(p1 + p2)
print(p2 - p3)
print(p3 * p4)
