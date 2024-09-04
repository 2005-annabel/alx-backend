#!/usr/bin/env python3
"""
This module implements a LFU caching algorithm.
"""
from base_caching import BaseCaching


def get_lfu_key(lfu_dict):
    """
    Get the least frequently used item from a dictionary of items.

    Args:
        lfu_dict (dict): Dictionary of items to evaluate.

    Returns:
        The key of the least frequently used item.
    """
    lfu = None
    for key, stats in lfu_dict.items():
        if lfu is None:
            lfu = key
        else:
            lfu_stats = lfu_dict[lfu]
            less_accessed = stats["accessed"] < lfu_stats["accessed"]
            equal_access = stats["accessed"] == lfu_stats["accessed"]
            less_ranked = stats["rank"] < lfu_stats["rank"]
            if (less_accessed) or (equal_access and less_ranked):
                lfu = key
    return lfu


class LFUCache(BaseCaching):
    """
    This class inherits from BaseCaching and is a caching system.
    """
    def __init__(self):
        super().__init__()
        self.lfu_track = dict()
        self.RANK = 0

    def put(self, key, item):
        """
        Inserts a new key-value pair into the cache.

        Args:
            key (str): Key to insert into the cache.
            item (str): Value to insert into the cache.

        Returns:
            Nothing.
        """
        if (key is None) or (item is None):
            return

        key_not_found = key not in self.cache_data
        full_cache = len(self.cache_data) >= self.MAX_ITEMS
        if key_not_found and full_cache:
            lfu_key = get_lfu_key(self.lfu_track)
            try:
                del self.lfu_track[lfu_key]
                del self.cache_data[lfu_key]
            except Exception:
                raise Exception("Error while discradin LFU item.")
            print("DISCARD: {}".format(lfu_key))

        if key_not_found:
            self.lfu_track[key] = {"accessed": 0, "rank": 0}
        self.cache_data[key] = item
        self.lfu_track[key]["accessed"] += 1
        self.lfu_track[key]["rank"] = self.RANK
        self.RANK += 1

    def get(self, key):
        """
        Retrieves a key-value pair from the cache.

        Args:
            key (str): Key to search for in the cache.

        Returns:
            Value associated with key in self.cache_data.
        """
        if key is None:
            return None

        if key in self.cache_data:
            self.lfu_track[key]["accessed"] += 1
            self.lfu_track[key]["rank"] = self.RANK
            self.RANK += 1
        return self.cache_data.get(key)
