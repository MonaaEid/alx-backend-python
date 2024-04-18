#!/usr/bin/env python3
"""type-annotated function element_length that takes a list lst as argument"""
from typing import List, Tuple
from typing import Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[tuple[str, int]]:

    return [(i, len(i)) for i in lst]
