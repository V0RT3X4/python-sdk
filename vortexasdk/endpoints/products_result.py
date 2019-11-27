import os
from multiprocessing.pool import Pool
from typing import List

import pandas as pd

from vortexasdk.api import Product
from vortexasdk.api.entity_flattening import flatten_dictionary
from vortexasdk.api.search_result import Result


class ProductResult(Result):
    """Container class that holds the result obtained from calling the `Product` endpoint."""

    def to_list(self) -> List[Product]:
        """Represent products as a list."""
        list_of_dicts = super().to_list()

        with Pool(os.cpu_count()) as pool:
            return list(pool.map(Product.from_dict, list_of_dicts))

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent products as a `pd.DataFrame`.

        # Arguments
            columns: The product features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'layer.0', 'parent.0.name']`.


        # Returns
        `pd.DataFrame` of products.

        """
        if columns is None:
            columns = DEFAULT_COLUMNS

        flattened_dicts = [flatten_dictionary(p) for p in super().to_list()]

        if columns == "all":
            return pd.DataFrame(data=flattened_dicts)
        else:
            return pd.DataFrame(data=flattened_dicts, columns=columns)


DEFAULT_COLUMNS = ["id", "name", "layer.0", "parent.0.name"]
