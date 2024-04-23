#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def runtime(n: int, max_delay: int) -> float:
    """
    Function that measures the total runtime and returns it.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
