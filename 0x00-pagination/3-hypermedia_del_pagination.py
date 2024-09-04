#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Gets the correct page from the dataset

        Args:
            index (int, optional): index of the page. Defaults to None.
            page_size (int, optional): number of items per page.
                                        Defaults to 10.

        Returns:
            Dict: dictionnary of the following format:
            {
                "index": <first_current_index>,
                "next_index": <next_index>,
                "page_size": <page_size>,
                "data": <page_of_the_dataset>
            }
        """
        assert type(index) == int and index >= 0
        indexed_dataset: Dict[int, List] = self.indexed_dataset()
        assert index < len(indexed_dataset)
        if page_size == 0:
            return {
                "index": index,
                "next_index": index,
                "page_size": 0,
                "data": []
            }

        data: List[List] = []
        i: int = index
        p_size: int = page_size
        while p_size > 0 and i < len(indexed_dataset):
            if i in indexed_dataset.keys():
                data.append(indexed_dataset[i])
                p_size -= 1
            i += 1

        return {
            "index": index,
            "next_index": i if i < len(indexed_dataset) else None,
            "page_size": len(data),
            "data": data
        }
