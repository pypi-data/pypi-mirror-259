from itertools import islice
from typing import Iterable


def batched(iterable: Iterable, n: int):
    "Batch data into tuples of length n. The last batch may be shorter."
    # batched("ABCDEFG", 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")

    it = iter(iterable)
    while True:
        batch = tuple(islice(it, n))
        if not batch:
            return
        yield batch
