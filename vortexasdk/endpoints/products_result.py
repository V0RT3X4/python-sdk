from typing import List

import pandas as pd

from vortexasdk.api import Product
from vortexasdk.api.search_result import Result


class ProductResult(Result):
    """Container class that holds the result obtained from calling the `Product` endpoint."""

    def __init__(self, records):
        super().__init__(records=records, return_type=Product)

    def to_list(self) -> List[Product]:
        """Represent products as a list."""
        return super().to_list()

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent products as a `pd.DataFrame`.

        # Arguments
            columns: The product features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'layer.0', 'parent.0.name']`.


        # Returns
        `pd.DataFrame` of products.

        """
        return super().to_df(columns=columns)
