import os
from typing import List

import pandas as pd

from vortexasdk.api import Attribute
from vortexasdk.api.search_result import Result
from vortexasdk.logger import get_logger

logger = get_logger(__name__)


class AttributeResult(Result):
    """Container class that holds the result obtained from calling the `Attributes` endpoint."""

    def to_list(self) -> List[Attribute]:
        """Represent attributes as a list."""
        list_of_dicts = super().to_list()

        logger.debug(f"Converting dictionary to AttributeResult using {os.cpu_count()} processes")
        return list(map(Attribute.from_dict, list_of_dicts))

    def to_df(self, columns=None) -> pd.DataFrame:
        """
        Represent attributes as a `pd.DataFrame`.

        # Arguments
            columns: The attributes features we want in the dataframe. Enter `columns='all'` to include all features.
            Defaults to `columns = ['id', 'name', 'type']`.


        # Returns
        `pd.DataFrame` of attributes.

        """
        if columns is None:
            columns = DEFAULT_COLUMNS

        if columns == "all":
            return pd.DataFrame(data=super().to_list())
        else:
            return pd.DataFrame(data=super().to_list(), columns=columns)


DEFAULT_COLUMNS = ["id", "name", "type"]
