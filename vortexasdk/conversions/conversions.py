from typing import List

from vortexasdk.api import ID
from vortexasdk.api.id import split_ids_other
from vortexasdk.api.shared_types import IDsNames
from vortexasdk.logger import get_logger
from vortexasdk.operations import Search
from vortexasdk.utils import convert_to_list

logger = get_logger(__name__)


def _convert_to_ids(ids_or_names: IDsNames, searcher: Search) -> List[ID]:
    """Convert containing a mix of IDs and names to a list of IDs."""
    ids_or_names_list = convert_to_list(ids_or_names)

    ids, others = split_ids_other(ids_or_names_list)
    if len(others) == 0:
        return ids
    else:
        return ids + _search_ids(searcher, term=others)


def _search_ids(searcher: Search, **kwargs) -> List[ID]:
    """Find IDs matching a given list of search terms."""
    logger.info(
        f"Searching {searcher.__class__.__name__} matching search terms: {kwargs}"
    )

    results = searcher.search(**kwargs)

    id_to_name = {r["id"]: r["name"] for r in results}

    logger.info(
        f"Found {len(results)} {searcher.__class__.__name__}: {id_to_name}"
    )

    return list(id_to_name.keys())
