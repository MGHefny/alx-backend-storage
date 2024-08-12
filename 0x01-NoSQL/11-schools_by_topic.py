#!/usr/bin/env python3
"""Task 11"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """returns list school"""
    record = mongo_collection.find({"topics": topic})
    return list(record)
