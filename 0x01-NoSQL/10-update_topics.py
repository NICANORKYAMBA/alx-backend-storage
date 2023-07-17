#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon July 17 14:50:00 2023

@Author: Nicanor Kyamba
"""


def update_topics(
        mongo_collection,
        name: str, topics: list) -> None:
    """
    Updates the topics of a collection.

    Args:
        mongo_collection (Collection): The collection to update.
        name (str): The name of the collection.
        topics (list): The new topics of the collection.
    """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
