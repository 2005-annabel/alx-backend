#!/usr/bin/env python3
"""
This module implements a LIFO caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO cache eviction system that inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()
        self.item_stack = list()

    def put(self, key, item):
        """
        Inserts a new key-value pair into the cache

        Args:
            key: key for the dictionary
            item: value to assign to the key

        Returns:
            Nothing
        """
        if (key is None) or (item is None):
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_key = self.item_stack.pop()
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))
            self.item_stack.append(key)

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves a key-value pair from the cache

        Args:
            key: key to retrieve from the cache

        Returns:
            Value in cache linked to key, or None if key not found
        """
        return self.cache_data.get(key)
