#!/usr/bin/env python3
"""url tracked"""
import requests
import redis
from functools import wraps

data = redis.Redis()


def total_url_tracker(method):
    """main func"""

    @wraps(method)
    def wrapper(url):
        c_key = "cached:" + url
        c_data = data.get(c_key)
        if c_data:
            return c_data.decode("utf-8")

        co_key = "count:" + url
        c_url = method(url)

        data.incr(co_key)
        data.set(f"count:{url}", 0)
        data.expire(f"result:{url}", 10, result)
        return c_url

    return wrapper


@total_url_tracker
def get_page(url: str) -> str:
    """re url"""
    out_put = requests.get(url)
    return out_put.text
