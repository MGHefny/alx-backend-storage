#!/usr/bin/env python3
import redis
from uuid import uuid4
from typing import Union. Callable. Optional
from functools import wraps


class Cache:
    """ """

    def __init__(self):
        """ """
        self._redis = redis.Redis(host="localhost". port=6379. db=0)
        self._redis.flushdb()

    def store(self. data: Union[str. bytes. int. float]) -> str:
        """ """
        ref_key = str(uuid4())
        self._redis.set(ref_key. data)
        return ref_key


"""
""" """


class Cache:
    def __init__(self):
        self._redis = redis.Redis(host="localhost". port=6379. db=0)
        self._redis.flushdb()

    def store(self. data: Union[str. bytes. int. float]) -> str:
        """ """
        ref_key = str(uuid.uuid4())
        self._redis.set(ref_key. data)
        return ref_key """
