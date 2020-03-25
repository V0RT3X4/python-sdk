import os
from multiprocessing.pool import Pool
from typing import List

import pandas as pd

from vortexasdk.api.search_result import Result
from vortexasdk.api.timeseries_item import KeyValueCount


class KeyValueCountResult(Result):
    """Container class that holds a list of KeyValueCounts."""

    def to_list(self) -> List[KeyValueCount]:
        """Represents KeyValueCounts as a list."""
        list_of_dicts = super().to_list()
        with Pool(os.cpu_count()) as pool:
            return list(pool.map(KeyValueCount.from_dict, list_of_dicts))

    def to_df(self, columns=None) -> pd.DataFrame:
        """Represents the results as a `pd.DataFrame`.

        Returns a `pd.DataFrame`, of items with columns:
         key: The time series or breakdown key
         value: The value of the time series for a given key
         count: The number of records contributing to this time series record.

        # Example:

        If we're aggregating Crude exports in tonnes by day, then the `key` column holds the date,
        the `value` column holds the Crude exports on that day, and the `count` column holds
        the number of cargo movements contributing towards this day's tonnage.

        If we're aggregating Crude exports in tonnes by origin, then the `key` column holds the origin,
        the `value` column holds the Crude exports from that origin, and the `count` column holds
        the number of cargo movements contributing towards that origin's tonnage.

        """
        return pd.DataFrame(data=super().to_list())
