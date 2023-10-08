# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> functools.reduce()

import functools

letters = ['h', 'e', 'l', 'l', 'o']

word = functools.reduce(lambda x, y: x+y, letters)
print(word)

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x*y, factorial)
print(result)
