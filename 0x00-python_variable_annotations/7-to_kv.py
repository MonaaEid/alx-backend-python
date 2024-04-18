#!/usr/bin/python3
"""type-annotated function to_kv that takes a string k and an int OR float v
as arguments and returns a tuple"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[Union[str, float]]:
    return (k, v * v)
