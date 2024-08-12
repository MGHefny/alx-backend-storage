#!/usr/bin/env python3
import pymongo

"""mongoDB operations with Python"""


def list_all(mongo_collection):
    """all record in Python"""
    record = mongo_collection.find()

    if record.count() == 0:
        return []

    return record
