import os
from multiprocessing import Pool
from typing import Dict, List

import jsons
import pandas as pd

from vortexasdk.api import Corporation
from vortexasdk.api.search_result import Result


def _serialize_charterer(dictionary: Dict) -> Corporation:
    return jsons.loads(jsons.dumps(dictionary), Corporation)


class CharterersResult(Result):
    """Container class that holds the result obtained from calling the `Vessels` endpoint."""

    def to_list(self) -> List[Corporation]:
        """Represent vessels as a list."""
        list_of_dicts = super().to_list()

        pmap = Pool(os.cpu_count()).map

        return list(pmap(_serialize_charterer, list_of_dicts))

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent vessels as a `pd.DataFrame`.

        # Arguments
            columns: The vessel features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'imo', 'vessel_class']`.


        # Returns
        `pd.DataFrame` of vessels.

        """
        if columns is None:
            columns = ['id', 'name', 'imo', 'vessel_class']

        df = pd.DataFrame(super().to_list())

        if columns == 'all':
            return df
        else:
            return df[columns]
