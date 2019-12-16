from typing import List

import pandas as pd

from vortexasdk.api import Geography
from vortexasdk.api.search_result import Result


class GeographyResult(Result):
    """Container class that holds the result obtained from calling the `Geography` endpoint."""

    def __init__(self, records):
        super().__init__(records=records, return_type=Geography)

    def to_list(self) -> List[Geography]:
        """Represent geographies as a list."""
        return super().to_list()

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent geographies as a `pd.DataFrame`.

        # Arguments
            columns: The geography features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'layer']`.


        # Returns
        `pd.DataFrame` of geographies.

        """
        return super().to_df(columns=columns)
