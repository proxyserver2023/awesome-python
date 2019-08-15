from typing import NewType
A = NewType('Fuck', int)
s = A(1234)


def get_user(u: A) -> str:
    return 'Hello'


print(get_user(A(1)))
print(get_user(1))