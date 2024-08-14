#!/usr/bin/env python3
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps

"""task 2"""


def count_calls(method: Callable) -> Callable:
    """"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


"""task 0"""


class Cache:
    """Cache class"""

    def __init__(self):
        """store flush"""
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

        @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """re str"""
        ref_key = str(uuid4())
        self._redis.set(ref_key, data)
        return ref_key

    """task 1"""

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """convert info format"""
        info = self._redis.get(key)
        if fn:
            info = fn(info)
        return info

    def get_str(self, key: str) -> str:
        """correct func"""
        info = self._redis.get(key)
        return info.decode("utf-8")

    def get_int(self, key: str) -> int:
        """correct func"""
        info = self._redis.get(key)
        try:
            info = int(info.decode("utf-8"))
        except Exception:
            info = 0
        return info
