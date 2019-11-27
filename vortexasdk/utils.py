from typing import Dict, List


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
