The `try` statement works as follows:

1. first try clause is executed.
2. if no exception occurs the except caluse is skipped and execution of try statement is finished.
3. If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try statement.
4. If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with a message as shown above.

```python
try:
    pass
except (RuntimeError, TypeError, NameError):
    pass


class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
    
"""
Note that if the except clauses were reversed (with except B first), it would have printed B, B, B — the first matching except clause is triggered.
"""
```

```python

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
```


The else-clause runs when there is no exception but before the finally-clause. That is its primary purpose

```python
import sys


for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

```python

>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs

```

**Raising Statements**
```python
raise NameError('HiThere')
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# NameError: HiThere

```
**User Defined Exceptions**
```python
class Error(Exception):
    pass
    
class InputError(Error):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
        
class TransitionError(Error):
    def __init__(self, previous, next, message):
       self.previous = previous
       self.next = next
       self.message = message

```

**Defining Clean-up Actions**
```python
try:
    print('1')
    raise KeyboardInterrupt('This is a Message')
except NameError as inst:
    print(inst)
else:
    print("Gets for Everything")
finally:
    print('Goodbye, world!')
    
# A finally clause is always executed before leaving the try statement.
```

```python
try:
    print('A')
    raise 5/0
except NameError as e:
    print(e)
else:
    print('ELSE')
finally:
    print('FINALLY')
    
# A
# FINALLY
# Traceback (most recent call last):
#  File "/home/alamin/.virtualenvs/awesome-python/lib/python3.6/site-packages/IPython/core/interactiveshell.py", line 2961, in run_code
#    exec(code_obj, self.user_global_ns, self.user_ns)
#  File "<ipython-input-2-d18ed50e3f33>", line 3, in <module>
#    raise 5/0
# ZeroDivisionError: division by zero

```

```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

**Predefined Cleanup Actions**:
```python
for line in open('myfile.txt'):
    print(line, end="")

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

```

Another use-case for the else-clause is to perform actions that must occur when no exception occurs and that do not occur when exceptions are handled. For example:

```python
import logging

recip = float('Inf')
try:
    recip = 1 / 0
except ZeroDivisionError:
    logging.info('Infinite Result')
else:
    logging.info('Finite Result')

```

Lastly, the most common use of an else-clause in a try-block is for a bit of beautification (aligning the exceptional outcomes and non-exceptional outcomes at the same level of indentation). This use is always optional and isn't strictly necessary.
