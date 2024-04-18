#!/usr/bin/python3
"""function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier"""


def make_multiplier(multiplier: float) -> callable:
    """returns a function that multiplies a float by multiplier"""
    def multiply(n: float) -> float:
        """returns a float"""
        return n * multiplier
    return multiply
