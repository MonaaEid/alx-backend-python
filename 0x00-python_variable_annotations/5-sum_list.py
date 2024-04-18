#!/usr/bin/env python3
"""type-annotated function sum_list that takes a list input_list
of floats as argumentand returns their sum as a float"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns their sum as a float"""
    return sum(input_list)
