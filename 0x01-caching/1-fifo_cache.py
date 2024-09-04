#!/usr/bin/env python3
"""
This module implements a FIFO caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO cache eviction system that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        super().__init__()
        self.item_queue = list()

    def put(self, key, item):
        """
        Inserts a new key-value pair into the cache

        Arguments:
            key: key for the dictionary
            item: value to assign to the key

        Returns:
            Nothing
        """
        if (key is None) or (item is None):
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                first_key = self.item_queue.pop()
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))
            self.item_queue.insert(0, key)

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves a key-value pair from the cache

        Arguments:
            key: key to retrieve from the cache

        Returns:
            Value in cache linked to key, or None if key not found
        """
        return self.cache_data.get(key)
