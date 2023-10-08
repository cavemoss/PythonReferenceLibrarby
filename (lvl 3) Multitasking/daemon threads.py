# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> daemon threads

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print('you have been here for ' + str(count) + ' sec')
timer_thread = threading.Thread(target=timer, daemon=False)
# timer_thread.setDaemon(True)
# print(timer_thread.isDaemon())
timer_thread.start()

input('input anything to stop the daemon\n')
