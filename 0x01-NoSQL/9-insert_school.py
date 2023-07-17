#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon July 17 14:32:00 2023

@Author: Nicanor Kyamba
"""
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs) -> str:
    """
    Insert a school

    Args:
        mongo_collection (Collection): pymongo collection
        **kwargs (dict): school data

    Returns:
        str: id of the inserted school
    """
    return str(mongo_collection.insert_one(kwargs).inserted_id)
