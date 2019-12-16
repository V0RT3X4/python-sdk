import os
from typing import Dict, List, Callable, Any
from multiprocessing import Pool


def convert_to_list(a) -> List:
    """Convert wraps element in list if element isn't a list already."""
    if a is None:
        return []
    elif isinstance(a, list):
        return a
    else:
        return [a]


def convert_values_to_list(data: Dict) -> Dict:
    """Convert each value to a list."""
    return {k: convert_to_list(v) for k, v in data.items()}


def run_as_multiprocess(method: Callable, data: Any):
    """Execute a callable method on a set of data using all CPU cores"""
    with Pool(os.cpu_count()) as pool:
        return pool.map(method, data)
