def countdown(num):
    while num > 0:
        num -= 1


COUNT = 50000000
import time
start = time.time()
countdown(COUNT)
end = time.time() - start
print(end)
