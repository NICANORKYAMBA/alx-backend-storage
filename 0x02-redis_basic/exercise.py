#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed July  19 12:40:00 2023

@Author: Nicanor Kyamba
"""
import uuid
from typing import Union, Callable, Optional
import redis


class Cache:
    """Cache class to store data in redis"""
    def __init__(self):
        """Initialize class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in cache"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Read from Redis and recovering original type"""
        original_data = self._redis.get(key)
        if fn:
            return fn(original_data)
        return original_data

    def get_str(self, key: str) -> str:
        """
        Automatically parametrizes Cache.data with the
        correct conversion function
        """
        original_data = self._redis.get(key)
        original_data.decode('utf-8')
        return original_data

    def get_int(self, key: str) -> int:
        """
        Automatically parametrizes Cache.data with the
        correct conversion function
        """
        original_data = self._redis.get(key)
        original_data = int(original_data)
        return original_data
