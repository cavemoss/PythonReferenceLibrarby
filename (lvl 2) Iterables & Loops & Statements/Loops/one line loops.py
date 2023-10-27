# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> one line loops

[print(i+1) for i in range(10)]
print('\n')

[print(i) for i in range(50, 100+1, 2)]
print('\n')

[print(i) for i in 'thisisitbois']
print('\n')

import time
def count(val):
    print(val)
    time.sleep(1)  
[count(sec) for sec in range(10, 0, -1)]
print('happy!')          
