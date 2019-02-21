"""
>>> print(dir())
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> import struct
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'struct']
>>> dir(struct)
['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_clearcache', 'calcsize', 'error', 'iter_unpack', 'pack', 'pack_into', 'unpack', 'unpack_from']
>>> list(set(dir(struct)) - set(dir()))
['pack', 'Struct', 'unpack', '_clearcache', 'error', 'iter_unpack', '__all__', 'pack_into', 'unpack_from', '__cached__', 'calcsize', '__file__']
>>> list(set(dir(struct)).intersection(set(dir())))
['__builtins__', '__name__', '__doc__', '__loader__', '__package__', '__spec__']
"""
print(dir())
print(dir(complex))