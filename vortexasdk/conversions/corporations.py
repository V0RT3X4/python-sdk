from typing import List, Union

from vortexasdk.endpoints.corporations import Corporations
from vortexasdk.api import ID
from vortexasdk.conversions.conversions import _convert_to_ids


def convert_to_corporation_ids(
    ids_or_names_list: List[Union[ID, str]]
) -> List[ID]:
    """
    Convert a mixed list of names or IDs to charterer ids.

    # Example
    ```
    >>> convert_to_corporation_ids(["Exon"])
    [...]

    ```
    """
    return _convert_to_ids(ids_or_names_list, Corporations())
