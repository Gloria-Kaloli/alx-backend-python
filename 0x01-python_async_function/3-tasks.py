#!/usr/bin/env python3
""" function task_wait_random that takes an integer max_delay
and returns a asyncio
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asynchronous task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
