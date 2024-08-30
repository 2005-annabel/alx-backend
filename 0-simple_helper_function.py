#!/usr/bin/env python3
"""
This python script create a function that reads the number of
pages in a book
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[Tuple]:
    """ Function that reads the number of a page
    page: (int) - number of page
    page_size: (int) - total page size

    return: (tuple)
    """
    if page <= 0 or page > page_size:
        return None
    if page_size == 0:
        return (page, page_size)
        # I can instead return page and page
    page_start = (page - 1) * page_size
    page_end = page_start + page_size
    return (page_start, page_end)
