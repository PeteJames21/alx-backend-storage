#!/usr/bin/env python3
"""Defines a function that lists all documents in a collection."""

from pymongo.collection import Collection


def list_all(mongo_collection: Collection):
    """List all documents in the collection."""
    return list(mongo_collection.find({}))
