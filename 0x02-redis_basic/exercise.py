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
    """Initialize class Cache"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self,
              data: Union[str, bytes, int, float]) -> str:
        """Store data in cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
