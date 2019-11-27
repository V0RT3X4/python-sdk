"""Vessels Endpoint."""
from typing import List, Union

from vortexasdk.api.id import ID
from vortexasdk.conversions import convert_to_product_ids
from vortexasdk.endpoints.endpoints import VESSELS_REFERENCE
from vortexasdk.endpoints.vessels_result import VesselsResult
from vortexasdk.operations import Reference, Search
from vortexasdk.utils import convert_to_list


class Vessels(Reference, Search):
    """Vessels endpoint."""

    def __init__(self):
        """Instantiate endpoint using reference endpoint."""
        Reference.__init__(self, VESSELS_REFERENCE)
        Search.__init__(self, VESSELS_REFERENCE)

    def search(
        self,
        term: Union[str, List[str]] = None,
        ids: Union[str, List[str]] = None,
        vessel_classes: Union[str, List[str]] = None,
        vessel_product_types: Union[str, List[str]] = None,
    ) -> VesselsResult:
        """
        Find all vessels matching given search arguments. Search arguments are combined in an AND manner.

        # Arguments
            term: The name(s) (or partial name(s)) of a vessel we'd like to search

            ids: ID or IDs of vessels we'd like to search

            vessel_classes: vessel_class (or list of vessel classes) we'd like to search. Each vessel class must be one of "tiny_tanker" , "general_purpose" , "handysize" , "handymax" , "panamax" , "aframax" , "suezmax" , "vlcc_plus" , "sgc" , "mgc" , "lgc" , "vlgc". Refer to [ VortexaAPI Vessel Entities](https://docs.vortexa.com/reference/intro-vessel-entities) for the most up-to-date list of vessel classes.

            vessel_product_types: A product, or list of products to filter on, searching vessels currently carrying these products. Both product names or IDs can be entered here.

        # Returns
        List of vessels matching the search arguments.


        # Examples

        - Let's find all the VLCCs with 'ocean' in their name, or related names.

        ```python
        >>> from vortexasdk import Vessels
        >>> Vessels().search(vessel_classes='vlcc', term='ocean').to_df(columns=['name', 'imo', 'mmsi', 'related_names'])
        ```

        |    | name         |     imo |      mmsi | related_names             |
        |---:|:-------------|--------:|----------:|:--------------------------|
        |  0 | OCEANIS      | 9532757 | 241089000 | ['OCEANIS']               |
        |  1 | AEGEAN       | 9732553 | 205761000 | ['GENER8 OCEANUS']        |
        |  2 | OCEANIA      | 9246633 | 205753000 | ['OCEANIA'| 'TI OCEANIA'] |
        |  3 | ENEOS OCEAN  | 9662875 | 432986000 | ['ENEOS OCEAN']           |
        |  4 | OCEAN LILY   | 9284960 | 477178100 | ['OCEAN LILY']            |
        |  5 | SHINYO OCEAN | 9197868 | 636019316 | ['SHINYO OCEAN']          |
        |  6 | NASHA        | 9079107 | 370497000 | ['OCEANIC']               |
        |  7 | HUMANITY     | 9180281 | 422204700 | ['OCEAN NYMPH']           |

        Note the `term` search also looks for vessels with matching `related_names`


        - Let's find all the vessels currently carrying Crude.

        ```python
        >>> Vessels().search(vessel_product_types='crude').to_df()
        ```

        # Further Documentation

        [VortexaAPI Vessel Reference](https://docs.vortexa.com/reference/POST/reference/vessels)

        """
        search_params = {
            "term": [str(e) for e in convert_to_list(term)],
            "ids": convert_to_list(ids),
            "vessel_classes": convert_to_list(vessel_classes),
            "vessel_product_types": convert_to_product_ids(
                convert_to_list(vessel_product_types)
            ),
        }

        return VesselsResult(super().search(**search_params))

    def reference(self, id: ID):
        """
        Perform a vessel lookup.

        # Arguments
            id: Vessel ID to lookup

        # Returns
        Vessel record matching the ID

        # Further Documentation:
        [VortexaAPI Vessel Reference](https://docs.vortexa.com/reference/GET/reference/vessels/%7Bid%7D)

        """
        return super().reference(id)


AVAILABLE_VESSEL_CLASSES = [
    "tiny_tanker",
    "general_purpose",
    "handysize",
    "handymax",
    "panamax",
    "aframax",
    "suezmax",
    "vlcc_plus",
    "vlcc",
    "sgc",
    "mgc",
    "lgc",
    "vlgc",
]
