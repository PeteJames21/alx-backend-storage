#!/usr/bin/env python3
"""Defines a function that lists all documents in a collection."""


def list_all(mongo_collection):
    """List all documents in the collection."""
    return list(mongo_collection.find({}))
