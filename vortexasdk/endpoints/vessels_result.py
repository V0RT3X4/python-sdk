from typing import List

import pandas as pd

from vortexasdk.api import Vessel
from vortexasdk.api.search_result import Result


class VesselsResult(Result):
    """Container class that holds the result obtained from calling the `Vessels` endpoint."""

    def __init__(self, records):
        super().__init__(records=records, return_type=Vessel)

    def to_list(self) -> List[Vessel]:
        """Represent vessels as a list."""
        return super().to_list()

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
