a = 'string'
b = 42
c = 4.2
d = True

print(

    len(a), a.__len__(),

    b + 8, b.__add__(8),
    b - 2, b.__sub__(2),

    str(c), c.__str__(),
    int(c), c.__int__()

)
