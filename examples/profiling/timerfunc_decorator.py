# -*- coding: utf-8 -*-
# Simple Timer Function


def timefunc(f):
    def f_timer(*args, **kwargs):
        import time
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__,
              'took',
              end - start,
              'seconds')
        return result
    return f_timer


def get_number():
    return 10


@timefunc
def expensive_function():
    for x in get_number():
        i = x ^ x ^ x

    return 'Some Result'


result = expensive_function()
print(result)