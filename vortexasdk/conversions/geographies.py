from typing import List, Union

from vortexasdk.endpoints.geographies import Geographies
from vortexasdk.api import ID
from vortexasdk.conversions.conversions import _convert_to_ids


def convert_to_geography_ids(
    ids_or_names_list: List[Union[ID, str]]
) -> List[ID]:
    """
    Convert a mixed list of names or IDs to geography ids.

    # Example
    ```
    >>> convert_to_geography_ids(["Rotterdam [NL]"])
    [...]

    ```

    # Example
    ```
    >>> convert_to_geography_ids(["Rotterdam [NL]", "b514a3bfd0b87d91984f43d9ee5071fb3a063ec309f2fe486ca3d2e58b61d683"])
    [...]

    ```

    """
    return _convert_to_ids(ids_or_names_list, Geographies())
