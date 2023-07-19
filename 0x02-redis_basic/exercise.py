#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed July  19 12:40:00 2023

@Author: Nicanor Kyamba
"""
import uuid
from typing import Union
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
