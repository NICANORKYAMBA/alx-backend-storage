#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed July  19 19:00:00 2023

@Author: Nicanor Kyamba
"""
import redis
import requests
from functools import wraps

r = redis.Redis()


def url_access_count(method):
    """ Decorator for counting """
    @wraps(method)
    def wrapper(url):
        """ Wrapper for decorator """
        key = "cached:" + url
        cached_value = r.get(key)
        if cached_value:
            return cached_value.decode("utf-8")

            # Get new content and update cache
        key_count = "count:" + url
        html_content = method(url)

        r.incr(key_count)
        r.set(key, html_content, ex=10)
        r.expire(key, 10)
        return html_content
    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """ Obtain the HTML content of a  URL """
    results = requests.get(url)
    return results.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
