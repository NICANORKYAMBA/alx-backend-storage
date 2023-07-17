#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon July 17 14:32:00 2023

@Author: Nicanor Kyamba
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a school

    Args:
        mongo_collection (Collection): pymongo collection
        **kwargs (dict): school data

    Returns:
        str: id of the inserted school
    """
    return mongo_collection.insert(kwargs)
