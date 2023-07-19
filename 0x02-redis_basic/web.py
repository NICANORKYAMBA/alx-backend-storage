#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed July  19 19:00:00 2023

@Author: Nicanor Kyamba
"""
import time
from functools import wraps
import requests


"""Cache dictionary to store URL responses"""
cache:  = {}


def get_page(url: str) -> str:
    """
    Check if URL response is already cached and
    within expiration time
    """
    if url in cache and time.time() - cache[url]['timestamp'] < 10:
        cache[url]['count'] += 1  # Increment access count
        return cache[url]['content']

    """Make a request to obtain the HTML content"""
    response = requests.get(url)
    content = response.text

    """Cache the response with access count and timestamp"""
    cache[url] = {
        'content': content,
        'count': 1,
        'timestamp': time.time()
    }

    return content


def cache_and_track(func):
    """Decorator to cache and track URL accesses"""
    @wraps(func)
    def wrapper(url):
        """
        Check if URL response is already cached
        and within expiration time
        """
        if url in cache and time.time() - cache[url]['timestamp'] < 10:
            cache[url]['count'] += 1
            return cache[url]['content']
        else:
            content = func(url)
            cache[url] = {
                'content': content,
                'count': 1,
                'timestamp': time.time()
            }
            return content

    return wrapper


@cache_and_track
def get_page_with_decorator(url: str) -> str:
    """Using the decorator to implement get_page function"""
    response = requests.get(url)
    return response.text
