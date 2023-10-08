# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> random module

import random

print(random.randint(1, 6))
print(random.random())

move = ['rock', 'paper', 'scissors']
print(random.choice(move))

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
random.shuffle(cards)

for i in cards:
    print(i, end=' ')
