from typing import List, Union

from vortexasdk.endpoints.products import Products
from vortexasdk.api import ID
from vortexasdk.conversions.conversions import _convert_to_ids


def convert_to_product_ids(
    ids_or_names_list: List[Union[ID, str]]
) -> List[ID]:
    """
    Convert a mixed list of names or IDs to vessel ids.

    # Example
    ```
    >>> convert_to_product_ids(["crude"])
    [...]

    ```
    """
    return _convert_to_ids(ids_or_names_list, Products())
