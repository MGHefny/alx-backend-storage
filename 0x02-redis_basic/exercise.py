#!/usr/bin/env python3
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps

"""task 0"""


class Cache:
    """Cache class"""

    def __init__(self):
        """store flush"""
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """re str"""
        ref_key = str(uuid4())
        self._redis.set(ref_key, data)
        return ref_key
