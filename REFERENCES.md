# References

## Reserved Classes of Identifiers

1. `_*` Not imported by from module import \*
2. `__*__` System Defined Names
3. `__*` class-private names.

## is vs equal

1. `==` checks for equality
2. `is` checks for identity

```python
a = [1,2,3]
b = a
a == b  # contents of a and b are equal ? => True
a is b # is a and b pointing to the same object => TRUE
c = list(a)
a == c # True
a is c # False
```

## site packages vs dist packages

- **site-packages** - installed by pip or python
- **dist-packages** - installed by system's package-manager like `apt`.
