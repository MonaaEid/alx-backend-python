#!/usr/bin/env python3
"""comment :)"""
import typing
from typing import Union, Tuple, NoneType


def safe_first_element(
        lst: typing.Sequence[typing.Any]) -> typing.Union[typing.Any, NoneType]:
    """returns the first element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
