#!/usr/bin/env python3
"""comment"""
import asyncio
from typing import List
import time
aysnc_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that will execute async_comprehension four times in parallel
    using asyncio.gather.
    """
    start = time.time()
    await asyncio.gather(*(aysnc_comprehension() for _ in range(4)))
    end = time.time()
    return (end - start)
