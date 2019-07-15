from functools import wraps


def third_decorator(f):
    print('Called -2')
    @wraps(f)
    def third_wrapper(*args, **kwargs):
        print('Calling Decorated Funcs')
        return f(*args, **kwargs)
    return third_wrapper


def second_decorator(f):
    print('Called -1')
    return f


def first_decorator(f):
    print('Called 0')
    return f


@first_decorator
@second_decorator
@third_decorator
def example():
    """Docstring"""
    print('Called 1')


example()
print(example.__name__)
print(example.__doc__)