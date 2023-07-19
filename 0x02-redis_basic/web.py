#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed July  19 19:00:00 2023

@Author: Nicanor Kyamba
"""
from functools import wraps
import redis
import requests
from typing import Callable

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ Decorator for counting """
    @wraps(method)
    def wrapper(url):  # sourcery skip: use-named-expression
        """ Wrapper for decorator """
        key = "cached:" + url
        cached = r.get(key)
        if cached:
            return cached.decode('utf-8')

        key_count = "count:" + url
        result = method(url)

        r.incr(key_count)
        r.set(key, result, ex=10)
        r.expire(key, 10)
        return result

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ Obtain the HTML content of a  URL """
    req = requests.get(url)
    return req.text


if __name__ == "__main__":
    print(get_page("http://slowwly.robertomurray.co.uk"))
