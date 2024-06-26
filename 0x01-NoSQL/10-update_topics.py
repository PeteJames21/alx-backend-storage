#!/usr/bin/env python3
"""
Defines a function that updates all documents that match a certain filter.
"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name."""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
