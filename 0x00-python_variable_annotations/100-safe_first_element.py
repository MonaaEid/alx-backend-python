# The types of the elements of the input are not know

import typing
from typing import Union, Tuple, NoneType


def safe_first_element(lst: typing.Sequence[typing.Any]) -> typing.Union[typing.Any, NoneType]:
    if lst:
        return lst[0]
    else:
        return None
