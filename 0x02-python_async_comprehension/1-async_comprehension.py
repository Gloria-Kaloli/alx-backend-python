#!/usr/bin/env python3
"""The coroutine will collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers."""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension- function to return 10 random numbers
    Arguments:
        no arguments
    Returns:
        10 random numbers
    """
    rslt = [i async for i in async_generator()]
    return rslt
