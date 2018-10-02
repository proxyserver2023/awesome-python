import functools

def myfunc(a, b=2):
    "Docstring for myfunc()."
    print(a, b)

def show_details(name, f):
    try:
        print(f.__name__)
    except AttributeError:
        print('no __name__')

    print('__doc__', repr(f.__doc__()))


show_details('myfunc', myfunc)

p1 = functools.partial(myfunc, b=4)
show_details('raw_wrapper', p1)


print('Updating wrapper:')
print('  assign:', functools.WRAPPER_ASSIGNMENTS)
print('  update:', functools.WRAPPER_UPDATES)
print()


functools.update_wrapper(p1, myfunc)
show_details('updated wrapper', p1)