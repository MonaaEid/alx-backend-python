#!/usr/bin/env python3
"""type-annotated function type_checking that takes a variable x, and returns the
sum as a float"""
from typing import Union, Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """returns a zoomed in list"""
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
