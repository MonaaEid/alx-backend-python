#!/usr/bin/python3
"""type-annotated function element_length that takes a list lst as argument
and returns a list of tuples representing each element and its length"""


def element_length(lst: list[str]) -> list[tuple[str, int]]:
    """returns a list of tuples representing each element and its length"""
    return [(i, len(i)) for i in lst]
