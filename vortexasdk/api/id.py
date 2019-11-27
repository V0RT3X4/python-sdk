import re
from typing import List, Tuple

ID = str


def is_valid_id(potential_id) -> bool:
    """Check if argument is valid SHA256 hash."""
    return (
        isinstance(potential_id, str)
        and re.match("^[A-Fa-f0-9]{64}$", potential_id) is not None
    )


def split_ids_other(ids_or_other: List) -> Tuple[List[ID], List]:
    """Extract IDs and names from a list, returning a list of IDs, and a list of names."""
    ids = []
    others = []

    for item in ids_or_other:
        if is_valid_id(item):
            ids.append(item)
        else:
            others.append(item)

    return ids, others
