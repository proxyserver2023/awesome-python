def countdown(num):
    while num > 0:
        num -= 1


COUNT = 50000000
import time, threading
start = time.time()
t1 = threading.Thread(target=countdown, args=(COUNT//2,))
t2 = threading.Thread(target=countdown, args=(COUNT//2,))
end = time.time() - start
print(end)
