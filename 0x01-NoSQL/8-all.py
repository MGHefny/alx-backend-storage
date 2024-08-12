#!/usr/bin/env python3
"""mongoDB operations with Python"""
import pymongo


def list_all(mongo_collection):
    """all record in Python"""
    if not mongo_collection:
        return []
    record = mongo_collection.find()
    return [push for push in record]
