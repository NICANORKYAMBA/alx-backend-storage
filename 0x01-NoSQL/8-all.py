#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon July  17 14:22:25 2023

@Author: Nicanor Kyamba
"""
from typing import List


def list_all(mongo_collection) -> List[dict]:
    """
    List all documents in a collection

    Args:
        mongo_collection (Collection): collection to list

    Returns:
        List[dict]: list of documents
    """
    documents = []
    for document in mongo_collection.find():
        documents.append(document)
    return documents
