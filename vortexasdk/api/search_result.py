import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Any
from functools import partial
from multiprocessing import Pool

from vortexasdk.api.geography import Geography
from vortexasdk.api.product import Product
from vortexasdk.api.vessel import Vessel
from vortexasdk.api.corporation import Corporation

import jsons
import pandas as pd


class Result:
    MULTI = False

    def __init__(self, records, endpoint, default_columns):
        self.records = records
        self.endpoint = endpoint
        self.default_columns = default_columns

    @property
    def endpoint(self):
        return self.__endpoint

    @endpoint.setter
    def endpoint(self, endpoint_value):
        permitted_endpoints = {
            Geography, Product, Vessel, Corporation
        }
        if endpoint_value not in permitted_endpoints:
            raise ValueError(f"{endpoint_value} is not a permitted dataclass")
        else:
            self.__endpoint = endpoint_value

    @property
    def default_columns(self):
        return self.__default_columns

    @default_columns.setter
    def default_columns(self, default_col_values):
        self.__default_columns = default_col_values

    def to_list(self):
        if not self.MULTI:
            # standard to list
            output_list = self._serialize_endpoint(self.records, List[self.endpoint])
        else:
            multi_serialize = partial(self._serialize_endpoint, data_class=self.endpoint)
            # pool to list
            pmap = Pool(os.cpu_count()).map
            output_list = list(pmap(multi_serialize, self.records))
        return output_list

    def to_df(self, columns=None):
        df = pd.DataFrame(self.records)
        columns = columns or self.default_columns

        if columns == "all":
            return df
        else:
            return df[columns]

    @staticmethod
    def _serialize_endpoint(data, data_class):
        return jsons.loads(jsons.dumps(data), data_class)

    def __len__(self):
        """Delegate to *_records*."""
        return len(self.records)

    def __str__(self):
        """Delegate to *_records*."""
        return str(self.records)

    def __iter__(self):
        """Delegate to *_records*."""
        return iter(self.records)

    def __getitem__(self, item):
        """Delegate to *_records*."""
        return self.records.__getitem__(item)
