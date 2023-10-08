# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> math module

import math

a = 2
b = 3
c = 4
pi = 3.14

values = [
    round(pi),              # round (round a number)
    math.ceil(pi),          # math.ceil (round a number up)
    math.floor(pi),         # math.floor (round a number down)
    abs(pi),                # abs (return absolute value)
    pow(pi, 2),             # pow (return arg_one to the power of arg_two)
    math.sqrt(420),         # math.sqrt (return the square root)
    max(a, b, c),           # max (return the biggest item)
    min(a, b, c)            # min (return the smallest item)
]

for i in values:
    print(i)
