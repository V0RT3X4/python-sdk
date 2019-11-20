"""Vessels Endpoint."""
import os
from multiprocessing import Pool
from typing import List, Union, Dict

import jsons
import pandas as pd

from vortexasdk.api.id import ID
from vortexasdk.api.search_result import Result
from vortexasdk.api.vessel import Vessel
from vortexasdk.endpoints.endpoints import VESSELS_REFERENCE
from vortexasdk.operations import Reference, Search
from vortexasdk.utils import convert_values_to_list


def _serialize_vessel(dictionary: Dict) -> Vessel:
    return jsons.loads(jsons.dumps(dictionary), Vessel)


class VesselsResult(Result):
    """Container class that holds the result obtained from calling the `Vessels` endpoint."""
    DEFAULT_COLUMNS = ['id', 'name', 'imo', 'vessel_class']

    def to_list(self) -> List[Vessel]:
        """Represent vessels as a list."""
        list_of_dicts = super().to_list()

        pmap = Pool(os.cpu_count()).map

        return list(pmap(_serialize_vessel, list_of_dicts))

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent vessels as a `pd.DataFrame`.

        # Arguments
            columns: The vessel features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'imo', 'vessel_class']`.


        # Returns
        `pd.DataFrame` of vessels.

        """
        return super().to_df(columns=columns)


class Vessels(Reference, Search):
    """Vessels endpoint."""

    def __init__(self):
        """Instantiate endpoint using reference endpoint."""
        Reference.__init__(self, VESSELS_REFERENCE)
        Search.__init__(self, VESSELS_REFERENCE)

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

    def search(self,
               term: Union[str, List[str]] = None,
               ids: Union[str, List[str]] = None,
               vessel_classes: Union[str, List[str]] = None,
               vessel_product_types: Union[str, List[str]] = None,
               ) -> VesselsResult:
        """
        Find all vessels matching given search terms.

        # Arguments
            term: The name(s) (or partial name(s)) of a vessel we'd like to search

            ids: ID or IDs of vessels we'd like to search

            vessel_classes: vessel_class (or list of vessel classes) we'd like to search. Each vessel class must be one of "tiny_tanker" | "general_purpose" | "handysize" | "handymax" | "panamax" | "aframax" | "suezmax" | "vlcc_plus" | "sgc" | "mgc" | "lgc" | "vlgc". Refer to [ VortexaAPI Vessel Entities](https://docs.vortexa.com/reference/intro-vessel-entities) for the most up-to-date list of vessel classes.

            vessel_product_types: product ID (or list of product IDs), searching vessels currently (or recently) carrying these products.

        # Returns
        List of vessels matching the search arguments.


        # Examples

        Let's find all the VLCCs with 'ocean' in their name, or related names.

        ```python
        >>> Vessels().search(vessel_classes='vlcc', term='ocean').to_df(columns=['name', 'imo', 'mmsi', 'related_names'])
        ```

        |    | name         |     imo |      mmsi | related_names             |
        |---:|:-------------|--------:|----------:|:--------------------------|
        |  0 | OCEANIS      | 9532757 | 241089000 | ['OCEANIS']               |
        |  1 | AEGEAN       | 9732553 | 205761000 | ['GENER8 OCEANUS']        |
        |  2 | OCEANIA      | 9246633 | 205753000 | ['OCEANIA', 'TI OCEANIA'] |
        |  3 | ENEOS OCEAN  | 9662875 | 432986000 | ['ENEOS OCEAN']           |
        |  4 | OCEAN LILY   | 9284960 | 477178100 | ['OCEAN LILY']            |
        |  5 | SHINYO OCEAN | 9197868 | 636019316 | ['SHINYO OCEAN']          |
        |  6 | NASHA        | 9079107 | 370497000 | ['OCEANIC']               |
        |  7 | HUMANITY     | 9180281 | 422204700 | ['OCEAN NYMPH']           |

        Note the `term` search also looks for vessels with matching `related_names`


        # Further Documentation

        [VortexaAPI Vessel Reference](https://docs.vortexa.com/reference/POST/reference/vessels)

        """
        search_params = convert_values_to_list({
            "term": term,
            "ids": ids,
            "vessel_classes": vessel_classes,
            "vessel_product_types": vessel_product_types,
        })

        return VesselsResult(super().search(**search_params))
