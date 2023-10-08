# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> while

FOREVER = True

while FOREVER:
    print('help ')

name = input('what is your name? ')
while len(name) == 0:
    name = input('what is your name? ')
print('hello '+name)

name = None
while not name:
    name = input('give me your name: ')
print('your name is '+name)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> for

for i in range(10):
    print(i + 1)
print('\n')

for i in range(50, 100+1, 2):
    print(i)
print('\n')

for i in 'thisisitbois':
    print(i)
print('\n')

import time                                        
for sec in range(10, 0, -1):
    print(sec)
    time.sleep(1)                 
print('happy!')
