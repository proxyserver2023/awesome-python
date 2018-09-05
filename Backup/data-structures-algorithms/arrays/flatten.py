"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""
from collections import Iterable


def flatten_returns_list(input_array, output_array=None):
    if output_array is None:
        output_array = []
    for element in input_array:
        if isinstance(element, Iterable):
            flatten_returns_list(element, output_array)
        else:
            output_array.append(element)
    return output_array


def flatten_returns_iterator(iterable):
    """
    Takes as input multi dimensional iterable and
    returns generator which produces one dimensional output.
    """
    for element in iterable:
        if isinstance(element, Iterable):
            yield from flatten_returns_iterator(element)
        else:
            yield element
