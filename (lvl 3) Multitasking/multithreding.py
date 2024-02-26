# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> multithreading

import threading
from threading import Thread
import time


# breakfast()
# coffee()
# study()

def breakfast():
    time.sleep(3)
    print('you eat breakfast')
thread_x = Thread(target=breakfast, args=())
thread_x.start()


def coffee():
    time.sleep(4)
    print('you drank coffee')
thread_y = Thread(target=coffee, args=())
thread_y.start()


def study():
    time.sleep(5)
    print('you finish studying')
thread_z = Thread(target=study, args=())
thread_z.start()

# thread_x.join()
# thread_y.join()
# thread_z.join()

print(threading.active_count())
print(threading.enumerate())
# print(time.perf_counter())
