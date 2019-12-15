from typing import List, Union

from vortexasdk.api import ID
from vortexasdk.api.id import split_ids_other
from vortexasdk.conversions.conversions import _search_ids
from vortexasdk.endpoints.vessels import AVAILABLE_VESSEL_CLASSES, Vessels
from vortexasdk.utils import convert_to_list


def convert_to_vessel_ids(
    vessel_attributes: Union[List[Union[ID, str, int]], ID, str, int]
) -> List[ID]:
    """
    Convert a mixed list of names, IDs, IMOs, or MMSIs to vessel ids.

    # Example
    ```
    >>> convert_to_vessel_ids(["Stallion", 9464326, 477639900, 'vlcc'])
    [...]

    ```
    """

    vessel_attributes_list = convert_to_list(vessel_attributes)
    ids, others = split_ids_other(vessel_attributes_list)

    vessel_classes = []
    names_imos_mmsis = []
    for e in others:
        if _is_vessel_class(e):
            vessel_classes.append(e)
        else:
            names_imos_mmsis.append(e)

    vessels_matched_on_vessel_class = (
        _search_ids(Vessels(), vessel_classes=vessel_classes)
        if len(vessel_classes) > 0
        else []
    )

    vessels_matched_on_name_imo_mmsi = (
        _search_ids(Vessels(), term=names_imos_mmsis)
        if len(names_imos_mmsis) > 0
        else []
    )

    return (
        ids
        + vessels_matched_on_vessel_class
        + vessels_matched_on_name_imo_mmsi
    )


def _is_vessel_class(potential_vessel_class) -> bool:
    return (
        isinstance(potential_vessel_class, str)
        and potential_vessel_class.lower() in AVAILABLE_VESSEL_CLASSES
    )
