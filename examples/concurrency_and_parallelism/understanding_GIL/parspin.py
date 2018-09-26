from threading import Thread
from subprocess import Popen

import time


def countdown(n):
    if n > 0:
        n -= 1

# Launch a useless process that spins
p = Popen(['python', 'spin.py'])
COUNT = 500000000000000000000000000000000000000
t1 = Thread(target=countdown, args=(COUNT//3,))
t2 = Thread(target=countdown, args=(COUNT//3,))
t3 = Thread(target=countdown, args=(COUNT//3,))
start = time.time()
t1.start(); t2.start(); t3.start()
t1.join(); t2.join(); t3.join()
end =time.time()
print(end-start)
p.terminate()
