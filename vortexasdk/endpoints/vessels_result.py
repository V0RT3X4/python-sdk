import os
from multiprocessing import Pool
from typing import List

import pandas as pd

from vortexasdk.api import Vessel
from vortexasdk.api.search_result import Result


class VesselsResult(Result):
    """Container class that holds the result obtained from calling the `Vessels` endpoint."""

    def to_list(self) -> List[Vessel]:
        """Represent vessels as a list."""
        list_of_dicts = super().to_list()

        with Pool(os.cpu_count()) as pool:
            return list(pool.map(Vessel.from_dict, list_of_dicts))

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
            columns = DEFAULT_COLUMNS

        if columns == "all":
            return pd.DataFrame(data=super().to_list())
        else:
            return pd.DataFrame(data=super().to_list(), columns=columns)


DEFAULT_COLUMNS = ["id", "name", "imo", "vessel_class"]
