#!/usr/bin/env python3
"""type-annotated function safely_get_value that takes a dict and a key as
arguments and returns the value of the key"""
from typing import Union, Any, Dict


def safely_get_value(dct: Dict, key: Any, default: Union[Any, None] = None) -> Union[Any, None]:
    """returns the value of the key"""
    if key in dct:
        return dct[key]
    else:
        return default
    

def safely_get_value(dct, key, default = None):
    """returns the value of the key"""
    if key in dct:
        return dct[key]
    else:
        return default