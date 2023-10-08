class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def __len__(self):
        import math
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    def length(self):
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __gt__(self, p):
        return self.length() > p.length()
    
    def __ge__(self, p):
        return self.length() >= p.length()
    
    def __lt__(self, p):
        return self.length() < p.length()

    def __le__(self, p):
        return self.length() <= p.length()
    
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'


p1 = Point(5, 5)
p2 = Point(4, 3)
p3 = Point(1, 2)
p4 = Point(-3, -5)

print(p1 == p2)
print(p2 > p3)
print(p3 <= p4)
print(len(p4))
