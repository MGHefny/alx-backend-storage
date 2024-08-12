#!/usr/bin/env python3
"""Insert data Python"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert data"""
    record = mongo_collection.insert_one(kwargs)
    return record.inserted_id
