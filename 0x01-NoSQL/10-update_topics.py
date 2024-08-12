#!/usr/bin/env python3
"""mongoDB Operations with Python"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Changes school topics"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
