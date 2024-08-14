#!/usr/bin/env python3
"""method 0x02. Redis basic"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps

"""task 2"""


def count_calls(method: Callable) -> Callable:
    """class called"""
    c_key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """return wrapper"""
        self._redis.incr(c_key)
        return method(self, *args, **kwargs)

    return wrapper


"""task 3"""


def call_history(method: Callable) -> Callable:
    """class called"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """return wrapper"""
        b_key = method.__qualname__
        i_key = b_key + ":inputs"
        o_key = b_key + ":outputs"
        i_info = str(args)
        self._redis.rpush(i_key, i_info)
        output = method(self, *args, **kwargs)
        o_info = str(output)
        self._redis.rpush(o_key, o_info)
        return output

    return wrapper


"""task 4"""


def replay(method: Callable):
    """replay abrove function"""
    re_get = redis.Redis()

    b2_key = method.__qualname__

    i2_key = b2_key + ":inputs"
    o2_key = b2_key + ":outputs"

    info_i = re_get.lrange(i2_key, 0, -1)
    info_o = re_get.lrange(o2_key, 0, -1)

    coun = len(info_i)
    """"""
    print("{} was called {} times:".format(b2_key, coun))
    """"""
    for inp, out in zip(info_i, info_o):
        print(
            "{}(*{}) -> {}".format(
                b2_key,
                inp.decode("utf-8"),
                out.decode("utf-8"),
            )
        )


"""task 0"""


class Cache:
    """Cache class"""

    def __init__(self):
        """store flush"""
        self._redis = redis.Redis(host="localhost", port=6379, db=0)
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """re str"""
        ref_key = str(uuid4())
        self._redis.set(ref_key, data)
        return ref_key

    """task 1"""

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
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
