#!/usr/bin/env python3
"""comment"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns the first element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
