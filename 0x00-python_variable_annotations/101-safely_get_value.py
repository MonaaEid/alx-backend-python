#usr/bin/env python3
"""type-annotated function safely_get_value that takes a dict and a key as
arguments and returns the value of the key"""
from typing import Union, Any, Dict


def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default