from typing import List

import pandas as pd

from vortexasdk.api import Corporation
from vortexasdk.api.search_result import Result


class CorporationsResult(Result):
    """Container class that holds the result obtained from calling the `Vessels` endpoint."""

    def __init__(self, records):
        super().__init__(records=records, return_type=Corporation)

    def to_list(self) -> List[Corporation]:
        """Represent vessels as a list."""
        return super().to_list()

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent corporations as a `pd.DataFrame`.

        # Arguments
            columns: The corporation features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'corporate_entity_type']`.


        # Returns
        `pd.DataFrame` of corporations.

        """
        return super().to_df(columns=columns)
