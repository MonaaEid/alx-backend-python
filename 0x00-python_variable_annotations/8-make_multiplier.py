#!/usr/bin/env python3
"""function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier"""


def make_multiplier(multiplier: float) -> callable:
    """returns a function that multiplies a float by multiplier"""
    return lambda n: n * multiplier
